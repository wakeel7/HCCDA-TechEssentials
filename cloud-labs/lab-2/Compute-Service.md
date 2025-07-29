
# HUAWEI CLOUD Compute Service

## Overview
This guide demonstrates how to deploy and manage Elastic Cloud Servers (ECS) using HUAWEI CLOUD's infrastructure services, with a focus on creating and utilizing custom images through the Image Management Service (IMS).

---

## 1. Initial Setup and ECS Deployment

### Network Foundation
1. **Create a Virtual Private Cloud (VPC)**:
   - Provides isolated network environment
   - Configure IP ranges and subnets
   - Set up route tables and gateways

### Server Provisioning
Deploy two server types with distinct configurations:

#### Windows ECS
- **Image**: Windows Server 2012 R2 (public image)
- **Configuration**:
  - Billing: Pay-per-use
  - Region: AP-Singapore
  - No Elastic IP (EIP) assigned initially
  - Set administrator password during creation

#### Linux ECS
- **Image**: CentOS 7.6 (public image)
- **Configuration**:
  - Auto-assign Elastic IP
  - Same region and billing model
  - Set root password during creation

### Server Management
- **Access Methods**:
  - Windows: Remote Desktop via VNC client
  - Linux: Command line via VNC terminal (user: root)
  
- **Resource Modification**:
  1. Stop the ECS instance
  2. Select "Modify Specifications"
  3. Choose new hardware configuration
  4. Restart to apply changes

---

## 2. Image Management Service (IMS)

### Creating Private Images
Transform configured ECS instances into reusable templates:

#### Windows Image Preparation
1. **Network Configuration**:
   - Set NIC to DHCP (automatic IP/DNS)
2. **Remote Access**:
   - Enable Remote Desktop
   - Configure firewall rules
3. **Initialization**:
   - Verify Cloudbase-Init installation

#### Linux Image Preparation
1. **Network Configuration**:
   - Ensure DHCP in network config files
2. **Initialization**:
   - Confirm Cloud-Init and password reset plugin
3. **Cleanup**:
   - Remove persistent network rules (`/etc/udev/rules.d`)

#### Image Creation Process
1. Navigate to IMS console
2. Select "Create System Disk Image"
3. Choose prepared ECS as source
4. Configure image metadata (name, description)

---

## 3. Advanced Image Operations

### Image Management
- **Metadata Editing**: Update names/descriptions
- **Regional Replication**: Create copies within same region
- **Version Control**: Maintain multiple image versions

### Image Sharing
1. Obtain recipient's Project ID
2. Select "Share" on private image
3. Add recipient's Project ID
4. Recipient accepts shared image in their account

### Deployment from Custom Images
1. Launch new ECS instance
2. Select your private image as source
3. Configure instance parameters
4. Deploy identical environment in minutes

---

## Best Practices
- **Security**: Always remove sensitive data before imaging
- **Documentation**: Maintain change logs for custom images
- **Testing**: Validate new images in staging before production
- **Tagging**: Use consistent naming conventions for images

(![IMG-20250727-WA0050](https://github.com/user-attachments/assets/78f9c9bc-383c-4acb-9169-b793323dff33)
![IMG-20250727-WA0049](https://github.com/user-attachments/assets/b3c78143-b520-47e3-a5df-32c2f93d8cf8)
![IMG-20250727-WA0048](https://github.com/user-attachments/assets/0884a416-49e1-4bfa-8f5f-a6833975b057)
![IMG-20250727-WA0047](https://github.com/user-attachments/assets/b76f0bc0-f36d-42bb-9e25-ff71a39b5cb1)
![IMG-20250727-WA0046](https://github.com/user-attachments/assets/75ad0bfe-5d20-4f68-8ee7-3df08c4f1f93)
![IMG-20250727-WA0045](https://github.com/user-attachments/assets/64c152a3-7274-4786-9160-050b0154f3d5)
![IMG-20250727-WA0044](https://github.com/user-attachments/assets/66723f5f-5ae4-48f2-853f-0414b4d35201)
![IMG-20250727-WA0043](https://github.com/user-attachments/assets/5566dc9d-9918-4578-a395-0e67b49703fe)
![IMG-20250727-WA0042](https://github.com/user-attachments/assets/1dda1e47-d197-4018-98af-9851fab29ac5)
![IMG-20250727-WA0041](https://github.com/user-attachments/assets/b9c0f2a1-6fba-469b-95fb-6996f3edc77a)
![IMG-20250727-WA0040](https://github.com/user-attachments/assets/e5a2a054-3bff-46b4-9129-9182fff115f4)
![IMG-20250727-WA0039](https://github.com/user-attachments/assets/accc5101-6833-41f9-8365-23011d564465)
![IMG-20250727-WA0052](https://github.com/user-attachments/assets/b3205a78-ad28-4fde-8ffa-ff228058dcc4)
![IMG-20250727-WA0051](https://github.com/user-attachments/assets/9b7c44a0-5491-441d-be2d-fe1e9d2d2215)
)
