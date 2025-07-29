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
    
  (<img width="913" height="564" alt="13" src="https://github.com/user-attachments/assets/13124435-67bf-4568-a827-a21dec7f8a3e" />
<img width="907" height="547" alt="12" src="https://github.com/user-attachments/assets/b3994f6f-98c7-4b61-8868-776a3dbc3eee" />
<img width="908" height="415" alt="11" src="https://github.com/user-attachments/assets/06c51574-6d51-40a1-afd6-14244a3a45d3" />
<img width="911" height="524" alt="10" src="https://github.com/user-attachments/assets/4ecbe5f7-ddf4-4501-91c9-8de5bd9880da" />
<img width="909" height="488" alt="9" src="https://github.com/user-attachments/assets/f0e2c439-a4ab-4bb0-bd8c-2604499ca2fa" />
<img width="906" height="397" alt="8" src="https://github.com/user-attachments/assets/a60c01d8-10cf-4d05-ba06-d4c004e91b06" />
<img width="910" height="422" alt="7" src="https://github.com/user-attachments/assets/f0defedc-96da-459e-9ee7-fa91a435d40e" />
<img width="909" height="418" alt="6" src="https://github.com/user-attachments/assets/495ee925-a329-465e-a09b-5ca5abdaa3a2" />
<img width="928" height="604" alt="5" src="https://github.com/user-attachments/assets/90cb6100-0449-4d4f-b850-25d20aed5905" />
<img width="915" height="453" alt="4" src="https://github.com/user-attachments/assets/71eb138d-fc0f-4c1c-8429-9f3d4c39b610" />
<img width="914" height="574" alt="3" src="https://github.com/user-attachments/assets/8cc30190-8a3c-4186-bc89-0ed05613591f" />
<img width="914" height="523" alt="2" src="https://github.com/user-attachments/assets/44396035-4734-41c0-86b8-6cc4b0990058" />
<img width="806" height="410" alt="1" src="https://github.com/user-attachments/assets/0c626442-c713-4763-8bff-dd0924be3695" />
<img width="906" height="433" alt="14" src="https://github.com/user-attachments/assets/c13fcc82-2aa4-44b4-8171-ee6a12705b08" />
)
