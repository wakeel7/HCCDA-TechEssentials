# Deploying a Scalable and Highly Available Enterprise Website on HUAWEI CLOUD

## 1. Network and Security Setup
To ensure a secure and isolated environment, we begin by creating a **Virtual Private Cloud (VPC)** in the **AP-Singapore region**. The VPC provides a private network with customizable IP ranges, subnets, route tables, and gateways. A default subnet is automatically created.

Next, a **security group** is configured, acting as a virtual firewall for **Elastic Cloud Servers (ECS)**. Using the **"General-purpose web server"** template, default rules are applied to allow:
- **HTTP (80)**
- **HTTPS (443)**
- **SSH (22)**
- **RDP (3389)**

For lab purposes, an additional rule permits all traffic (`0.0.0.0/0`), though stricter rules should be enforced in production.

---

## 2. Provisioning Compute and Database Resources
### Web Server (ECS)
- **Billing Model:** Pay-per-use
- **OS:** CentOS 7.6 64-bit
- **Network:** Placed in the configured VPC and security group
- **Public IP:** An **Elastic IP (EIP)** is auto-assigned for internet access.

### Database (RDS)
- **Engine:** MySQL 8.0 (Primary/Standby for high availability)
- **Network:** Same VPC and security group as the ECS for secure communication
- **Credentials:** Root password set during deployment
- **Access:** Floating IP noted for later use

---

## 3. Web Application Deployment (LAMP + WordPress)
1. **Remote Access:** Log in via **VNC** to the CentOS server.
2. **Install LAMP Stack:**
   - Use `yum` to install **Apache, MySQL (client), and PHP**.
   - Configure **Apache (`httpd.conf`)** with a `ServerName` directive.
3. **Deploy WordPress:**
   - Download and extract WordPress to `/var/www/html`.
   - Set proper file permissions.
   - Start and enable **Apache (`httpd`)** and **PHP-FPM** services.
4. **Database Setup:**
   - Access the **RDS instance** via **HUAWEI CLOUD’s Data Administration Service (DAS)**.
   - Execute:
     ```sql
     CREATE DATABASE wordpress;
     ```
5. **WordPress Installation:**
   - Access the site via the ECS’s public IP (`http://<ECS_IP>/wordpress`).
   - Enter database details:
     - **Database Name:** `wordpress`
     - **Username:** `root`
     - **Host:** RDS floating IP
   - Complete the setup by defining the site title and admin credentials.

---

## 4. Scaling with ELB and Auto Scaling (AS)
To handle traffic fluctuations:
### Elastic Load Balancer (ELB)
- Configure a **public-facing load balancer** in the VPC.
- Set up an **HTTP listener (port 80)** forwarding to a backend server group.

### Auto Scaling (AS)
1. **Create a Private Image:**
   - Use **Image Management Service (IMS)** to snapshot the configured ECS.
2. **Define AS Configuration:**
   - **Template:** The private image
   - **Instance Type & Security Group:** Match the original ECS
   - **No EIP assigned** (traffic routed via ELB)
3. **Configure AS Group:**
   - **Min Instances:** 1
   - **Max Instances:** 3
   - **Expected Instances:** 2
4. **Scaling Policies:**
   - **Scale Out:** If CPU > **60%**
   - **Scale In:** If CPU < **20%**

---

## 5. Verification and Monitoring
- **Access the Site:** Verify via the **ELB’s EIP** to confirm the full stack (ELB → Web Servers → RDS) is operational.
- **Monitoring with Cloud Eye:**
  - Track **CPU, disk I/O, and network metrics**.
  - Set up alarms for resource thresholds.
    
  (<img width="913" height="564" alt="13" src="https://github.com/wakeel7/HCCDA-TechEssentials/blob/ed1ee7dce16773702a7077b8d4685f156f54e27f/cloud-labs/lab-1/Images/Screenshot%202025-07-28%20223432.png" />
<img width="907" height="547" alt="12" src="https://github.com/wakeel7/HCCDA-TechEssentials/blob/ed1ee7dce16773702a7077b8d4685f156f54e27f/cloud-labs/lab-1/Images/Screenshot%202025-07-28%20223420.png" />
