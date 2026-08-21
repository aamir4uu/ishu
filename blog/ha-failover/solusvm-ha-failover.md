# What Happens When a Node Fails? A Look Inside SolusVM HA Failover

SolusVM detects a failed compute resource through its shared storage lock, not a network ping. Once that lock expires and the grace period passes, the surviving nodes in the failover domain confirm the failure and SolusVM restarts each affected virtual server on healthy hardware. Same IP, same disks, cold boot.

![Rows of servers in a data center rack, the hardware a SolusVM HA failover domain protects](https://www.pexels.com/photo/server-racks-on-data-center-5480781/)

[Image Source](https://www.pexels.com/photo/server-racks-on-data-center-5480781/)

## Key Takeaways

- HA failover is a restart, not a continuation. Your customers' virtual servers reboot. Anything held in memory is gone.
- Detection runs off the storage lock and a watchdog timer, so a network partition alone will not trigger an evacuation.
- Virtual servers are placed individually across the surviving nodes, so they may land on one host or several. Disks never move.
- Failback is manual. When the dead node returns, nothing comes home on its own.
- [Backblaze put the 2025 annualised drive failure rate at 1.36%](https://www.backblaze.com/blog/backblaze-drive-stats-for-2025/) across 344,196 drives. Drives are one component out of many in a node.

## How Does SolusVM Know a Compute Resource Has Failed?

This is the part most people get wrong, and it decides whether your cluster is safe or dangerous.

Every compute resource in a [failover domain](https://docs.solusvm.com/en/solusvm2/administrator-guide/high-availability/) holds a lock on the shared storage and keeps renewing it. A local watchdog enforces that renewal. Stop renewing and the watchdog fires, which expires the lock. Surviving nodes see that expiry directly, on the storage they all share. Confirmation held for longer than the grace period is what starts an evacuation.

Notice what is not in that chain: the management node's ability to reach the host.

If the management node loses network access to a compute resource but the resource still holds its storage lock, SolusVM treats it as alive and starts nothing. That behaviour looks conservative until you think about what the alternative does. A switch reboot would otherwise convince the cluster that six healthy hosts had died, and it would start their virtual servers a second time on other hardware while the originals were still writing to the same disks. Split brain corrupts filesystems quietly and you find out days later.

Storage is the arbiter here because storage is the thing that actually matters.

## What Happens to Your Virtual Servers During Failover?

Once the grace period expires, SolusVM places the affected virtual servers on the healthy compute resources in the same failover domain. It places each one individually, so they may all land on a single host or spread across several depending on what capacity is free.

Disks do not move, because they were always on shared storage rather than on the dead node. The IP address follows the virtual server, so DNS and customer configurations keep working. Anything that was running gets started again on the new host.

That last word is the one to be honest with customers about. Started, not resumed.

![Network cables connected to a server rack, the fabric a failover domain runs across](https://www.pexels.com/photo/ethernet-cables-plugged-on-a-server-rack-1054397/)

[Image Source](https://www.pexels.com/photo/ethernet-cables-plugged-on-a-server-rack-1054397/)

## What HA Failover Does Not Do

Sell it accurately and you get fewer angry tickets than the provider who implied something stronger.

It isn't live migration. A virtual server that goes down with its host comes back up cold, with an unclean shutdown behind it, so anything in RAM is lost and the guest filesystem replays its journal on boot.

Failback doesn't happen either. When the original compute resource returns to service, the virtual server keeps running where it landed, and moving it home is a manual operation you schedule.

Nor does any of this protect the storage. HA moves compute away from a dead node. If the shared storage itself goes down, every node in the domain is looking at the same outage, which is why the [storage design behind the failover domain](https://www.solusvm.com/blog/shared-storage-vs-local-storage-vps) deserves as much attention as the failover configuration on top of it.

## What You Have to Build Before Any of This Works

Requirements are short here, and none of them are negotiable.

A failover domain needs at least two compute resources, because a domain of one has nowhere to evacuate to. Every resource in it has to run KVM virtual servers on [Shared LVM over iSCSI or NFS](https://docs.solusvm.com/en/solusvm2/administrator-guide/adding-shared-lvm-storage/), and Virtuozzo compute resources are not supported even when the servers on them are KVM. Give each domain its own dedicated storage; sharing one storage backend across two domains is not a supported setup.

Then there's the capacity question, which is the one providers underestimate. Every node needs enough free CPU and memory to absorb the virtual servers from a failed peer. Run four nodes at 90% and a single failure has nowhere to put anything.

Finally, HA protection has to be enabled globally before any domain configuration does anything at all.

## When Failover Cannot Run: Disaster Recovery

HA and Disaster Recovery are separate features and they coexist deliberately.

If HA cannot place a virtual server, and that server has a valid backup, [Disaster Recovery](https://docs.solusvm.com/en/solusvm2/administrator-guide/disaster-recovery/) recreates and restores it onto healthy compute resources one at a time. It's slower than failover by a wide margin, because restoring means moving bytes rather than claiming a disk that's already there. It is also the only path available when the failure took the storage with it.

Configure both, and test the restore path on a server you can afford to lose, because a backup nobody has restored is a theory.

## Frequently Asked Questions

### How Long Does a SolusVM HA Failover Take?

Detection is bounded by the watchdog and the grace period you configure, then each virtual server boots. Budget the grace period plus a normal cold boot per server, and test it on your own hardware rather than trusting an estimate.

### Will Customers Notice a Failover?

Yes. Their server reboots and any in-memory state is lost. What they will not have to do is change an IP address or restore a backup themselves.

### Can a Network Outage Trigger a False Failover?

Not on its own. If the compute resource still holds its storage lock, SolusVM considers it active even when the management node cannot reach it. Evacuation waits on lock expiry, not on reachability.

### Do Virtual Servers Move Back Automatically After the Node Recovers?

No. They keep running where HA placed them. Moving them back to the original compute resource is a manual action.

### How Many Compute Resources Can One Failover Domain Hold?

Up to 2,000. Capacity headroom becomes the real limit long before that number does.

## What to Do With This

Work out what a node failure costs you today, in restore hours and in tickets, then compare that to the capacity headroom HA requires you to leave idle. Past a few racks the arithmetic is usually obvious. What deserves more care is what you tell customers, because "your server restarts on other hardware within minutes" is a promise you can keep and "no downtime" is not.

[See how High Availability and Disaster Recovery fit together in SolusVM](https://www.solusvm.com/features/).
