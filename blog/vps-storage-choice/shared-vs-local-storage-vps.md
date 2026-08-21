# Choosing Between Shared Storage and Local Storage for VPS Infrastructure

Use local storage when per-VPS disk speed is what you sell, and shared storage when you need live migration and automatic failover. Local NVMe answers reads in tens of microseconds. Network storage adds hundreds. That gap buys you the ability to move a running virtual server off a failing host without copying its data first.

![Server racks in a data center, the physical layer behind local and shared VPS storage](https://www.pexels.com/photo/server-racks-on-data-center-5480781/)

[Image Source](https://www.pexels.com/photo/server-racks-on-data-center-5480781/)

## Key Takeaways

- Local storage wins on latency, shared storage wins on recovery time, and nothing wins both.
- A local NVMe device answers a 4K read in roughly 20 to 70 microseconds. iSCSI-backed network storage lands in the hundreds.
- That penalty is an engineering outcome, not a law. An SPDK iSCSI target has hit 1.33 million IOPS against 1.55 million for the same drives locally.
- High Availability in SolusVM requires shared storage. Every compute resource in the failover domain has to run KVM and use Shared LVM over iSCSI, or NFS.
- Three-way replication returns roughly 33% of raw capacity as usable space. Budget for that before you quote a per-TB price.

## What the Two Models Actually Are

Local storage means the virtual disks live on the drives physically installed in the compute resource. SolusVM covers this with File-based, LVM and ThinLVM, which differ in how the host partitions its disk and packs data onto it. Nothing leaves the chassis.

Shared storage means several compute resources mount the same storage point, either NFS or Shared LVM presented over iSCSI targets. The virtual disk stops being tied to the host running it, which is the whole point and also the whole cost.

That one structural difference drives every trade-off below.

## How Much Performance Does Shared Storage Cost You?

Less than the folklore says, if you build the fabric properly. Considerably more if you don't.

Start with the device. Modern NVMe drives answer random 4K reads in about 20 to 70 microseconds. Put a network in the path and you add a round trip: [NVMe over TCP contributes roughly 250 to 450 microseconds](https://simplyblock.io/glossary/nvme-latency/), while conventional iSCSI stacks sit between several hundred microseconds and a full millisecond under load. That ratio looks alarming until you write it out as an absolute number: 0.4 milliseconds. Most web workloads will never notice it. A busy MySQL instance running small synchronous writes absolutely will.

Throughput holds up better than latency does. An SPDK iSCSI target has been measured at 1.33 million IOPS where the same local NVMe delivered 1.55 million. Losing 18% of peak IOPS is nothing like the 2x slowdown older SAN and NAS deployments earned their reputation with, and the difference is almost entirely network design: 25G or better, a dedicated storage VLAN, no oversubscription at the top of rack. Skimp on those and you get the folklore version.

## What Local Storage Costs You

A host dies at 03:00.

With local storage, every virtual server on it is down until that hardware comes back or until you restore from backup onto another node, and restoring means moving the actual bytes. On a node holding 4 TB of customer data, budget hours.

There's a second cost, and it shows up on the balance sheet rather than the status page. Local disks strand capacity. One compute resource sits at 85% while another has 40% free, and neither can lend to the other.

![Network cables plugged into a server rack, the fabric that shared VPS storage depends on](https://www.pexels.com/photo/ethernet-cables-plugged-on-a-server-rack-1054397/)

[Image Source](https://www.pexels.com/photo/ethernet-cables-plugged-on-a-server-rack-1054397/)

## Where SolusVM Draws the Line

SolusVM settles the argument in its own documentation. [High Availability in SolusVM](https://docs.solusvm.com/en/solusvm2/administrator-guide/high-availability/) requires that all compute resources in a failover domain run KVM virtual servers and use either Shared LVM over iSCSI or NFS. Local storage is not eligible. If automatic failover is on your feature list, shared storage isn't a preference, it's a prerequisite.

The reverse trade is documented just as plainly. [SolusVM's Shared LVM implementation](https://docs.solusvm.com/en/solusvm2/administrator-guide/adding-shared-lvm-storage/) does not support Thin LVM or snapshots, which means giving up thin provisioning and the incremental ThinLVM backups that keep backup storage costs flat as you grow. So the real question isn't which storage type is better. It's whether you want to sell failover or sell oversubscription, because on one compute resource you can't sell both. You can [move a server between storage types later](https://docs.solusvm.com/en/solusvm2/administrator-guide/migration-of-servers-between-compute-resources/), just not while it's running.

## Run Both, and Price the Difference

Most providers past their first rack end up running both, which is the right answer and not a fudge. Put your high-IOPS plans on local ThinLVM nodes, where thin provisioning and incremental backups hold the cost per customer down. Put your managed and business-tier plans on a shared LVM or NFS failover domain, where a dead host means a restarted virtual server instead of a support queue.

Then charge for the second tier.

Be specific about how much more. Three-way replication returns roughly a third of raw capacity as usable space, so 480 TB of raw disk becomes about 160 TB you can sell. Add 25G networking and the CPU the storage path eats on every node. A shared tier priced off local-storage economics loses money quietly for a year before anyone notices.

## Frequently Asked Questions

### Is Local Storage Always Faster Than Shared Storage?

At the device level, yes. In practice the gap depends on your fabric. A well-built NVMe over TCP or SPDK iSCSI target retains around 80% of local IOPS. A 1G iSCSI link to a spinning array will be several times slower than local disk.

### Can I Use Local Storage and Still Offer High Availability?

Not through the platform's HA feature. SolusVM requires Shared LVM over iSCSI or NFS for a failover domain. You can offer application-level redundancy across two local-storage instances on separate hosts, but that's a customer-side design.

### Does NFS Work for Production VPS Storage?

It works and SolusVM supports it, but NFS is a remote storage type and some operations take longer as a result. It's the lower-effort path into shared storage. Shared LVM over iSCSI is the faster one.

### What About Snapshots on Shared Storage?

The Shared LVM implementation in SolusVM doesn't support snapshots or Thin LVM, so if snapshot-based backups are part of your product, that constraint picks your storage type for you.

### Which Model Has the Lower Total Cost of Ownership?

Local storage, at small scale, by a wide margin. Shared storage catches up once stranded capacity across many nodes exceeds the replication overhead, and once manual recovery starts showing up in your ticket volume.

## Deciding

Pick the failure you can live with. Local storage costs you recovery time when hardware dies. Shared storage costs you microseconds on every I/O and a share of raw capacity to replication. Model both against the plans you actually sell, not against a benchmark. If the answer comes out mixed, build it mixed.

[See how SolusVM handles storage, migration and High Availability](https://www.solusvm.com/features/) across your compute resources.
