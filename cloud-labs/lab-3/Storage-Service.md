
# HUAWEI CLOUD Storage Services Practice

This project showcases **three fundamental storage services** offered by HUAWEI CLOUD:

- **Elastic Volume Service (EVS)**
- **Object Storage Service (OBS)**
- **Scalable File Service (SFS)**

The lab exercises are designed to provide **hands-on experience** in provisioning, managing, and utilizing these services to meet various business requirements.

---

## 🚀 Elastic Volume Service (EVS) Practice

**Elastic Volume Service (EVS)** provides **persistent block-level storage** for Elastic Cloud Servers (ECSs). EVS disks behave like physical hard drives and are used to **extend server storage**.

### 🔹 Key Concepts

- EVS disks must be in the **same Availability Zone (AZ)** as the ECS to be attached.
- EVS disks support **persistent data**, independent of any specific ECS.

### 🛠️ Windows ECS and EVS Workflow

1. **Network Setup**
   - Create a **Virtual Private Cloud (VPC)** and **subnet**.

2. **Provision ECS and EVS**
   - Launch a **Windows ECS**.
   - Purchase a **separate EVS data disk**.

3. **Attach and Initialize Disk**
   - Wait for the EVS disk to be in an **Available** state.
   - Attach the disk to the ECS.
   - Use **Disk Management** to:
     - Bring the disk **online**
     - Choose partition style (**MBR** or **GPT**)
     - Create and format a **New Simple Volume**

4. **Verify Persistence**
   - Create a test file on the new volume (e.g., D:\).
   - Take the disk **offline** in Windows OS.
   - Detach from ECS and **attach to a second Windows ECS**.
   - Log in and bring the disk online.
   - Confirm test file is present.

### 🐧 Linux ECS and EVS Workflow

1. **Provision ECS and Attach EVS**
   - Launch a **Linux ECS**.
   - Attach the EVS disk.

2. **Disk Initialization via CLI**
   - Use `fdisk` to create partition on `/dev/vdb`.
   - Format using `mkfs.ext4`.
   - Create a mount point directory (e.g., `/mnt/data`).
   - Use `mount` to attach the filesystem.
   - Edit `/etc/fstab` for **auto-mount at startup**.

3. **Using Snapshots**
   - Create a **snapshot** of the Linux EVS disk.
   - From the snapshot, **create a new EVS disk**.
   - Attach it to another ECS to verify snapshot restoration and cloning.

---

## ☁️ Object Storage Service (OBS) Practice

**OBS** provides storage for **massive unstructured data** (e.g., documents, images, videos) using an **object storage model**.

### 🔹 Bucket Operations

1. **Create a Bucket**
   - Define **region**, **storage class** (e.g., Standard), and **access policy** (e.g., Private).

2. **File Operations**
   - **Upload** files from local computer.
   - **Download** objects to local system.
   - **Delete** files and folders in the bucket.

This section builds foundational skills in **OBS console operations** and **data management**.

---

## 📁 Scalable File Service (SFS) Practice

**SFS** provides **high-performance, shared file storage**, ideal for environments requiring **simultaneous access** by multiple servers.

### 🔹 SFS Turbo Setup

1. **Create SFS Turbo**
   - Deploy the file system within the **existing VPC**.

2. **Mount on Linux ECS**
   - Install `nfs-utils`.
   - Use the `mount` command with **NFS protocol**.
   - Create a **shared directory** and a **test file**.

3. **Mount on Windows ECS**
   - Install **Client for NFS** via **Server Manager**.
   - Reboot the system.
   - Use `mount` in Command Prompt to map the SFS to a drive letter.
   - Confirm the test file created in Linux ECS is accessible.

---

## ✅ Conclusion

This hands-on project highlights how to:

- Provision and manage **block storage (EVS)** with snapshot capabilities
- Handle **object-based storage (OBS)** with bucket-based management
- Utilize **shared file systems (SFS)** for cross-platform access

These exercises equip users with practical knowledge to **effectively use Huawei Cloud storage services** in real-world scenarios.


![IMG-20250727-WA0033](https://github.com/wakeel7/HCCDA-TechEssentials/blob/986b69f54222c753b3a2b1624067c483334d8219/cloud-labs/lab-3/images/471241382-0a160373-fe3c-4627-9f60-959942bda6c4.jpg)
![IMG-20250727-WA0032](https://github.com/wakeel7/HCCDA-TechEssentials/blob/986b69f54222c753b3a2b1624067c483334d8219/cloud-labs/lab-3/images/471241378-5ca7ec7f-2617-4b81-a8b6-34e10b9d18a9.jpg)
![IMG-20250727-WA0031](https://github.com/wakeel7/HCCDA-TechEssentials/blob/986b69f54222c753b3a2b1624067c483334d8219/cloud-labs/lab-3/images/471241373-d1c2216a-6d58-4d36-acce-e8e576dc117a.jpg)
