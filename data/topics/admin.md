# Netskope Docs — Admin
_Generated: 2026-08-02 09:22 UTC_
_Pages: 56_

---
## About the Admin Console
**URL:** https://docs.netskope.com/en/about-the-admin-console/
**Last Modified:** 2025-08-31T01:50:45+00:00
**Scraped:** 2026-08-02T08:16:28.624650+00:00

About the Admin Console - Netskope Knowledge Portal
About the Admin Console
The Admin Console provides a central interface for configuring the settings of the Netskope Security Platform in addition to performing a variety of functions, like creating reports to managing incidents. To begin, log in your Netskope Tenant.
There are two primary areas of the Admin Console: Settings and Functions.
Settings
Settings are accessible by clicking
Settings
in the bottom of the left nav on the Home page.
This opens the Settings page, which provides general information.
The Settings page left nav panel contains these links:
Admin
Add admins to the management console, define and assign roles, and configure SSO and IP whitelist setting for the management console itself.
Security Cloud Platform
Configure the optional on-premises infrastructure components of the Netskope Active Platform in addition to managing client traffic steering deployments, reverse proxy configurations, and exceptions.
Risk Insights
Upload logs to your Netskope tenant. You can uploads logs directly via the UI or via SFTP. There is also a custom log parser.
API-enabled Protection
Configure API Introspection to connect to your IT-led, sanctioned cloud services.
Threat Protection
Options for configuring your Introspection-configured cloud services for malware protection in addition to configuring integration with Carbon Black.
Forensics
Enable forensics and setup a forensics profile.
Manage
Settings for traffic steering, custom apps, certificate-pinned apps, and device classification.
Tools
Create templates, configure directory tools, REST API, and clear events.
Functions
The Netskope Admin Console provides access to a number of functions. Functions are presented in the left nav panel.
Dashboard (Home)
Assess cloud risk by viewing information about applications, sites, users, total bytes, and total sessions. Customize this dashboard to display the information you want.
Incidents
The Incidents dashboard displays data loss prevention (DLP), anomalies, compromised credentials, malware, malicious sites, quarantine, and legal hold information.
API-enabled Protection
The API-enabled Protection dashboard provides visibility into file exposure for your sanctioned cloud services that have been configured with API Introspection. Assess your risk and optionally take action directly from the dashboard.
Policies
Implement inline and API Introspection policies, encryption, DLP, and threat protection. Customize policies with profiles and templates.
Skope IT
Use Skope IT, Netskope’s event-by-event monitoring tool, to view cloud usage events, manage alerts, interface with quarantine, legal hold, and threat threat protection dashboards, and manage incidents.
Cloud Confidence Index
Peruse the database of thousands of cloud services that have been researched and the enterprise-readiness assessed. Filter view by discovered apps or drill into the details of a specific cloud service.
Advanced Analytics
The Advanced Analytics dashboard displays summaries, and enables you to in-depth analysis and create custom reports.
In this Topic
About the Admin Console

---
## Access the Admin Console
**URL:** https://docs.netskope.com/en/access-the-admin-console/
**Last Modified:** 2025-08-31T01:50:47+00:00
**Scraped:** 2026-08-02T08:16:29.754906+00:00

Access the Admin Console - Netskope Knowledge Portal
Access the Admin Console
The Netskope Admin Console provides a central interface for configuring the settings of every aspect and feature the Netskope Cloud Security Platform has to offer; including creating policies, reviewing reports, and managing incidents.
The login URL to the Admin Console is unique for your company and different for every Netskope tenant. URLs the form:
https://
<tenant-name>
.goskope.com
https://
<tenant-name>
.au.goskope.com
https://
<tenant-name>
.eu.goskope.com
For example,
https://lightwave.goskope.com
and
https://lightwaveindustries.au.goskope.com
.
You will receive your login URL along with administrator credentials from your Netskope account representative upon creation of your account by email. If you have not received these, please contact support or your Netskope account team partner.
To learn more:
About the Netskope Admin Console
In this Topic
Access the Admin Console

---
## Create Local Administrators
**URL:** https://docs.netskope.com/en/create-local-administrators/
**Last Modified:** 2025-08-31T01:50:47+00:00
**Scraped:** 2026-08-02T08:17:35.553008+00:00

Create Local Administrators - Netskope Knowledge Portal
Create Local Administrators
Go to
Settings > Administration > Admins
and click
New Admin
.
Enter the email address of the administrator you would like to add, and select an appropriate role. For full
read-write
access, select the
Tenant Admin
role. For
read-only
access, select the
Restricted Admin
role.
For more information about adding a new administrator see the links below.
Managing Administrators
Create Roles for Restricted Administrators
Longer-term, we recommended that you integrate admin authentication with your company’s SSO provider (like Entra ID, Okta, etc). This can be managed via
Settings > Administration > SSO
.
Configure Single Sign On for the Netskope UI
IP Allowlisting can also be applied to your Netskope tenant to restrict the permitted source IP addresses that are allowed to connect to your Admin Console. This can be managed via
Settings > Administration > IP Allowlist
.
IP Allowlisting
In this Topic
Create Local Administrators

---
## Secure Tenant Configuration and Hardening
**URL:** https://docs.netskope.com/en/secure-tenant-configuration-and-hardening/
**Last Modified:** 2026-06-09T18:58:13+00:00
**Scraped:** 2026-08-02T08:18:33.497446+00:00

Secure Tenant Configuration and Hardening - Netskope Knowledge Portal
Secure Tenant Configuration and Hardening
This document outlines the security configurations available in Netskope products and how those can be used to harden the security of Netskope products and components deployed in customer environments.
Security hardening guidelines are provided in the following sections:
Tenant Security Hardening Guidelines
Client Security Hardening Guidelines
Private Access Security Hardening Guidelines
Publisher Security Hardening Guidelines
Appliance Security Hardening Guidelines
Cloud Exchange Security Hardening Guidelines
Tenant Security Hardening Guidelines
This section outlines the security configuration available in tenant UI and how those can be used to harden the security of UI.
User Identity and Authentication
User identity and access controls play an important role in how users are allowed to access the product and how the user’s identity will be established. Netskope provides these options to harden the user identity and access control to tenants.
Single Sign On (SSO)
Along with provisioning users locally, Netskope also provides capabilities to provision, identify, and authenticate users using the Single Sign On (SSO) solution. This solution provides an added security by providing the capability to control users’ access from one place, and removes the requirement of user management from each application.
To configure SSO:
In the Netskope UI, go to
Settings > Administration > SSO
.
Refer to
Configure Single Sign On for the Netskope UI
for the steps to configure SSO.
Multi-Factor Authentication (MFA)
To enhance the security of local users that are provisioned without SSO, Netskope provides an additional layer of security using multi-factor authentication. This protects user accounts from brute force attacks or compromised credentials attacks.
To configure MFA:
Go to
Settings > Administration > Admins
to open the Admins page to see the Types (1) and MFA Status (2) of an Admin.
Click the ellipses at the end of the local admin account user listing (3) and click
Edit
. The Edit Admin page opens.
Toggle the Multi-Factor Auth radio button from
Disabled
(default) to
Enabled
.
The next time the local admin logs in to their account, the admin must authenticate using an authentication app or a one-time password. Emails are sent to the email associated with the admin’s Netskope account.
If needed, you can reset the admin’s MFA. Click Reset to disable MFA for a local admin. You will see the following warning message.
Note:
Netskope recommends using either of the SSO or MFA features to protect users’ access to the tenant against any unauthorized attempts to access.
Concurrent Logins
Netskope provides a way to restrict users from logging into the same account from multiple devices. This ensures that in case a user’s account is compromised, the simultaneous login is prevented. It also gives a way for the user to track if the account is logged in at a different place or not.
To disallow concurrent logins:
To change the default, go to
Settings > Administration > Admins.
On the top right-hand side, click the
Settings
icon to open the Configure dialog box. Activate
Disallow Concurrent Logins by the same Admin.
Click
Save
.
Authorization/Access Control
Netskope provides a granular way to provide access to the users based on their roles and responsibilities. This ensures that a user gets access to what is really needed for them to work or access. The control is implemented via Role Based Access Control.
To configure Authorization/Access:
Go to
Settings > Administration > Roles
.
Refer to
Creating roles
to configure Role Based Access Control.
Brute Force Protections
Netskope provides a way to protect accounts from brute force attacks with additional configurations. The following sections explain the options.
IP Allowlisting
Netskope provides an option to restrict access to tenants based on IP address. This ensures that any unauthorized user is not able to access the tenant outside the customer’s IP address space.
To configure an IP allowlist:
Go to
Settings > Administration > IP Allowlist
and click
Edit.
Enter an IP address, range, or subnet. Multiple IP Addresses must be separated by a comma. When finished, click
+ADD.
Change the status from
Disabled
to
Enabled
.
Enable the IP allowlist and click
Save
.
Note
: Netskope has added a pre-defined list of Netskope’s IPs, which ensures Netskope Support is able to access the tenant to troubleshoot and resolve issues for customers.
Failed Login Attempts
This feature can be used to prevent users from brute force attempts, and ensures the account is locked out after a defined number of incorrect attempts.
To configure Failed Login Attempts:
Go to
Settings > Administration > Admins
.
Click
Settings
in the top right corner.
Enter the desired number of attempts for
Maximum failed login attempts
.
Click
Save
.
Additional Controls
Apart from the above controls, there are additional security measures that are available.
Idle Timeout
This feature enables administrators to logout users when the logged in session is inactive for a certain period of time. This can be configured to protect the tenant against abuses in scenarios where the user leaves the system unattended.
To configure Idle Timeout:
Go to
Settings > Administration > Admins
.
Click
Settings
in the top right corner.
Select the desired number of minutes on the
Idle Timeout
dropdown.
Click
Save
.
Password Expiration
A best practice is to expire passwords after a set interval to force users to rotate them.
To set how often a password expires:
Go to
Settings > Administration > Admins
.
On the top right-hand side, click the
Settings
icon.
Select the number of days on the
Password Expiration
dropdown.
Click
Save.
GovCloud
In the
PBMM
environment, the
CRL
Distribution point that performs certificate validation requires a client certificate, so add the
crl.govskope.ca
domain to your
SSL
DND (Do Not Decrypt) policies.
For details about
GovCloud
, go
here
.
Netskope Client Security Hardening Guidelines
The Netskope Client is the core of Netskope products and is used to steer traffic in your environments, provision access to private applications, and apply required security policies to end machines.
Considering the critical usage of Netskope Client, it is designed with a lot of security configurations and hardening options that you can leverage to adequately protect the Client in your environment.
The following sections explain the security configurations that are available in the Client.
User Identity and Authentication
The Netskope Client provides various ways to provision users, and establish user identity and user authentication. The users can be provisioned by using any of the following:
Using Netskope Directory Importer.
Using SCIM Application.
Manually.
For further details, please refer to detailed documentation
here
.
User identity in the Netskope Client is established using either of these parameters:
User principal name (UPN). This is automatically fetched for the user from the machine where the user is logged in.
User’s email address.
User authentication can be achieved by using either of these ways depending on how the Client is deployed and being provisioned for a user. Here are the user authentication methods supported by Netskope Client:
One-time token
: The Netskope Client uses a one-time token when the client is installed and provisioned using email invite. The email invite contains a one time token and after installation and user authentication is completed, the token expires. For more details, refer to the documentation
here
.
IdP-based authentication
: The Netskope Client supports user authentication and enrollment via IdP. In this case, the user will have to authenticate to the IdP configured for the tenant by the administrator. You can configure the IdP in SAML forward proxy. For more details, refer to the documentation
here
.
Authentication Token
: The Netskope Client provides tokens that can be used to establish the user authentication. The token is used as a shared secret between the Client and Netskope services to sign the JWT token, which is then used for user authentication. This token is part of Secure enrollment and can be leveraged by following the documentation
here
.
Note:
For strict enforcement of user authentication, it is recommended you enable the Secure Enrollment, and then Authentication Token in the Netskope UI.
Protection of Client Resources Post-Enrollment
Netskope provides various additional methods and features to protect the the Netskope Client and its resources after the deployment of the Client on an endpoint. Here are some of the those additional controls to further harden the Client.
Access Restrictions
You can prevent users from tampering with Netskope Client process, configuration files, registry, and directory location by accessing them on the endpoint. The access to all Netskope Client related files, processes, directories, etc. can be restricted. To add this additional protection:
Go to
Settings > Security Cloud Platform > Netskope Client > Client Configuration
.
Choose the Client configuration you want to edit.
Under
Tamperproof
, and check the box for
Protection Client configuration and resources
.
Click
Save
.
Encryption of Files
Apart from restricting users from accessing the files related to the Netskope Client, there is an option to encrypt the Netskope Client configuration files on the endpoint. This encryption uses the underlying operating system’s native encryption method to encrypt and decrypt the files.
To enable this feature, please reach out to the Netskope Support Team.
Note:
The above options are supported on Windows 10 and higher versions only.
Protection of Client Processes
The Netskope Client has various options to protect the Client’s processes, and have provisions to prevent users from disabling and removing the Client from their machines. The following sections explain these options.
Prevent Disabling of the Netskope Client
To avoid users bypassing the various policies and configurations that protect them while connected to the Netskope Client, it is important that users are unable to disable the Netskope Client themselves.
To prevent the disabling of the Netskope Client:
Go to
Settings > Security Cloud Platform > Client Configuration
Choose the Client configuration you want to edit.
Under
Tamperproof,
uncheck the box for
Allow disabling of Clients
.
Click
Save
Prevent Uninstallation of Netskope Client
It is also important that users are unable to uninstall the Netskope Client themselves. This can be done by protecting Client uninstallation with a password set by a tenant admin. On Windows devices, this password can also prevent the Client service from being stopped.
To prevent users from uninstalling the Client:
Go to
Settings > Security Cloud Platform > Netskope Client > Client Configuration
Choose the client configuration you want to edit.
Under
Tamperproof
, select
Password protect Client uninstallation
In the box that appears, type in the admin password that can be used if a scenario arises where the Netskope client needs to be uninstalled. Exercise proper password management hygiene when handling this password.
Click
Save
.
Note
: It is highly recommended to enable this setting along with
Protect Client configuration and resources
.
Protect an Endpoint in the Absence of a Client Tunnel
The Netskope Client has the capability to block all network traffic from an endpoint when certain scenarios are not met for the Client, such as:
A tunnel to steer the traffic from the Client to Netskope is not connected.
Users are not provisioned on the endpoint, but the Client is installed.
Enabling this setting prevents users from accessing the internet on the endpoint, ensuring that the endpoint is protected unless all security policies are configured on the machine.
Enabling this setting will also enable
Password protection Client uninstallation
and disable
Allow disabling of Clients
. This setting will honor all exceptions, except for category-based ones.
To enable this setting:
Go to
Settings > Security Cloud Platform > Netskope Client > Client Configuration
Choose the client configuration you want to edit.
Under
Tamperproof
, check the box for
Fail Close
.
If you have
Password protect Client uninstallation
disabled or
Allow disabling of Clients
enabled, the following message will appear. Click
Proceed.
Type in the Admin Password you want to use to protect the Client uninstallation. Then select whether:
Private App traffic should be excluded from being blocked
Notifications should show even if the client icon is hidden
How long Fail Close should be disabled for when a user is behind a captive portal.
Click
Save
.
Additional Controls
Apart from above controls, Netskope provides an additional control, like the capability to protect files during transmission.
Enrollment Configuration Protection
Enrollment configuration file can be protected additionally by encrypting on top of TLS. This ensures that confidentiality and integrity of the file is preserved while downloading, and prevents Client enrollment on machines where the decryption token is not configured.
To configure Secure Enrollment:
Go to
Settings > Security Cloud Platform > Netskope Client.
Click
MDM Distribution > Secure Enrollment
.
Enable
Enforce encryption of initial configuration of Netskope Client
.
This will create a token. Push the token on the end points using MDM/SCCM tools.
Updates and Upgrades
Netskope provides the capability to configure updates/upgrades for the Client, which ensures that the Client stays up-to-date in your environments. Keeping the software up-to-date with the latest version ensures that the security issues are patched and the application is using the latest features and functionalities.
To configure Upgrade settings:
Go to
Settings > Security Cloud Platform > Netskope Client > Client Configuration
.
Create or edit the configuration and go to
Install & Troubleshoot
.
Check the
Upgrade Client Automatically to
and select the updates from the dropdown.
Click
Save
.
Netskope Private Access (NPA) Security Hardening Guidelines
Netskope Private Access is provisioned using the Netskope Publisher and Netskope client. The Publisher is deployed near to the applications to which access needs to be provisioned. The access is provisioned using the NSClient for users where policies are configured and a separate tunnel is established to access the applications.
Below are some of the security hardening options available for Netskope Private Access apart from the inbuilt security controls:
User Authentication
Netskope establishes the authentication of the user with private applications through NSClient. Once the user is enrolled with NSClient, a separate authentication is initiated for the user to enroll with NPA and setup a NPA tunnel to provision access to applications.
Below are some options to harden the authentication for users for private apps:
Periodic Re-authentication for Private Apps
Periodic re-authentication ensures that users are re-authenticated using the idP configured for the tenant, after a specified time period to access the private apps. Without re-authentication, the users will not be able to access the private apps. This ensures that even if the device is compromised, a malicious user will not be able to access the apps.
Here are the steps to configure and use the feature:
Go to
Settings > Security Cloud Platform > Netskope Client > Client Configuration > New Client Configuration
Edit or create a new configuration for the users, and under
Private App Segment
, check
Periodic re-authentication for
Private App Segments
to enable it. Select an Interval and set a Grace Period. When finished, click
Save
.
Note
: If the option is not available please reach out to the Netskope Support team.
Netskope Publisher Security Hardening Guidelines
Netskope recommends below security hardening guidelines for NPA Publisher. Please configure these to harden the security of the publisher.
OS Hardening
Netskope provides NPA publisher with host os and also offers NPA publisher which can be installed on customer’s own host OS. For detailed information on the same, please refer
here
.
Netskope does below to harden the NPA publishers offered with host os:
Use CIS benchmarked image for host OS.
Disabled root login to base OS and container OS.
Removed root password.
Disabling support for CTL-ALT-DEL to prevent accidental or malicious system restarts.
Netskope recommends doing following things on the host OS to harden the publisher:
Access Hardening
Usage of key based authentication for SSH instead of password based authentication. Netskope AWS AMI does that out of the box.
Using the native Ubuntu 22.04 firewall or network firewalls to limit access to and from the Publisher.
Protocols and Ports
The Publisher requires communication over the following ports and protocols:
Port 22: SSH Access
Port 53: DNS Resolution
Port 443: HTTPS outbound connectivity for tunneling and updates
Any additional ports that are required by the customer applications.
Ensure that all other ports and protocols are disabled for the Publisher.
Updates and Upgrades
Netskope updates the host OS and the Publisher package during the software update process:
Base OS (Ubuntu 22.04) security updates and kernel updates.
Publisher (security, functionality, and enhancements). Netskope recommends that Publishers should always be updated to the most recent software version. Follow the instructions
here
for the kernel update.
Netskope provides a way to configure auto updates for Publishers. Follow the instructions
here
to configure and enable it.
Installation of 3rd-party Applications on Publishers
Netskope does not recommend installation of any 3rd-party software on Publishers, specifically on the ones where the host os is also provided by Netskope. Installation of any 3rd-party software should be done at a customers own risk and Netskope will not be responsible for any breach due the 3rd-party software installed by the customer. Follow the instructions
here
.
Publisher Maintenance Best Practices
Netskope provides a detailed guide on other publisher best practices to ensure the smooth functioning of the Publisher(s). Follow the best practices
here
.
Netskope Appliance Security Hardening Guidelines
Netskope recommends these security hardening guidelines for Netskope Appliance. These sections explain how to harden the security of the Appliance.
OS Hardening
Netskope has done these things to harden the OS by default for the appliance:
Restricted shell access.
By default, the access to the Appliance host OS is restricted to a limited number of commands.
Access Hardening
The Appliance comes with two user accounts, and both have default passwords. Netskope recommends that you change the default passwords for both accounts. Follow below instructions to do the same:
Log in to the Appliance using the default credentials.
After login, change the password by using the appropriate command:
For an nsadmin user:
nsappliance> auth change-password nsadmin
For an nstransfer user:
nsappliance> auth change-password nstransfer
Follow the pop up instructions on the shell afterwards to set the new password.
Ports and Services
Ensure that only these ports and services are configured on the Appliance and all others are disabled:
Outbound ports
Port 443: For management connectivity
Port 22: Log Upload using SFTP
Port 443: Log Upload to Netskope Cloud with HTTPS
Port 443: Use for fetching the REST API tokens with HTTPS
Inbound ports
Port 514: For receiving syslog traffic
Port 4400: AD Connector
Port 22: SFTP and SCP
Port 21: FTPS
Access Restriction using the IP Allowlist
SSH connections to access the Appliance CLI can be restricted to trusted IPs only. This configuration ensures that only allowlist IPs can access the Appliance CLI.
To configure allowlist IPs on an Appliance:
Log in to the Appliance.
Go to configuration mode by using the
configure
command.
In the configuration mode, use this command to set the IP allowlist.
set system ssh-allowlist
<comma-separated list of IPs and subnets without spaces>
Example:
set system ssh-allowlist 192.168.169.0/24,172.18.78.10
Enter
Save
.
Ensure these things exist to properly configure the IP Allowlist:
Subnets must be specified in this format:
<IP>/<Netmask>
. For example,
192.168.169.0/24, 172.18.78.0/255.255.255.0.
Individual allowlisted IPs in the list cannot be the same as IP addresses that are configured on the Appliance’s interfaces. Although, allowlisted subnets are allowed to contain IP addresses configured on the Appliance’s interfaces.
Allowlist IPs must not contain the subnet reserved for Netskope Appliance’s internal bridge network. By default, the Appliance’s internal services use the subnet
172.17.0.0/16
. This subnet can be changed using the command,
set system bridge-network
<IP subnet>
When specifying a new subnet for the bridge network, use the format
<Network Address>
/
<Netmask>
. For example:
192.168.1.0/0, 172.18.78.0/255.255.255.0.
Configure a Login Banner
When you log into your virtual appliance, the default login banner for the Netskope Appliance is displayed in the console. It is recommended to update the banner with your organization’s policies to deter malicious use of the software. Follow the instructions below to update:
To configure a login banner, enter the following command at the configuration prompt:
set system login-banner
Copy and paste the login banner at the prompt.
Press
Ctrl-D
to set the new login banner.
To save the login banner configuration, enter
save
at the configuration prompt.
Certificate Management
Appliance require server side certificates to enable SSL inspection. Appliance can generate self-signed certificates, but it is recommended to use CA signed certificates. Follow the below guide setup your CA signed certificates:
Log in to the Appliance.
Use these commands to set up the certificate:
set dataplane forward-proxy server-cert
(Copy paste the certificate and press Enter, then type Ctrl-D.)
set dataplane forward-proxy server-key
(Copy and paste your private key in the buffer, press Enter, then type Ctrl-D to exit.)
set dataplane forward-proxy server-intermediate-ca-chain
Copy and paste any additional certificates in the following order:
Server certificate, Intermediate CA certificate, Root CA certificate
Press
Enter
, then type
Ctrl-D
to exit.
Enter
Save
and press
Enter
to save the configuration.
Log Upload Hardening
The Appliance provides various methods to securely upload the logs. Netskope recommends that you configure these security methods.
Configure SSH Keys for Log Uploads
You can configure your SSH key pairs to automatically upload logs to the appliance.
To use your own SSH key pairs:
Log in to the Appliance.
Enter
configure
to enter the nsshell configure mode.
Add an entry to the ssh-public-keys list in the CLI configuration by using this command:
add log-upload ssh-public-keys
added index 0
Set the value of the ssh public key at the index returned from the last command. This requires you to paste the SSH public key:
set log-upload ssh-public-keys 0 key
Copy and paste the ssh public key.
Enter one or more lines of input. When done, press Ctrl-D.
To verify the configuration are applied properly, enter the following command:
show log-upload ssh-public-keys
Enter save to activate your changes.
For detailed information on various log upload options and configuration, go
here
.
Audit Logging and Monitoring
Netskope recommends that you monitor the logs of the appliance to detect any malicious activity. Appliances generate audit logs for all the actions and events generated by the user’s activities.
To monitor and set up alerts in Appliance logs:
Open nsshell to the Appliance and enter this command:
add audit-logging destinations
Server response should be added after index 0.
Use following commands to configure the syslog server destination:
set audit-logging destinations 0 host <hostname>
set audit-logging destinations 0 port <port number>
set audit-logging destinations 0 protocol [TCP | UDP]
set audit-logging enable true
Enter
false
in the last command to turn off this feature.
When enabled, review the log file on the system specified in the host and port commands.
Updates and Upgrades
Netskope recommends keeping the Appliance updated to the latest version. The latest version contains security bug fixes, functionality enhancements and other improvements. Refer to these instructions to upgrade and set up auto updates for the Appliance.
Upgrade
Set up auto-update
Cloud Exchange Security Hardening Guidelines
Netskope recommends these security hardening guidelines for Cloud Exchange. The following sections explain how to harden the security of the Cloud Exchange.
Host Hardening
Cloud Exchange can be deployed in various ways depending on customer requirements and environment. Netskope recommends hardening the underlying OS aligning with organizational policies using the OS supported security best practices such as:
Disabling unused and insecure ports.
Enabling certificate-based user authentication to the OS.
Ensuring proper logging and event management.
Keeping the OS updated with the latest security patches.
High Availability
Netskope provides an option to deploy and configure the Cloud Exchange in High Availability configurations to ensure the service is up and running in case of any failure or outage at one place. For more information in HA configuration, go
here
.
Netskope recommends that you use this feature and apply these best practices:
Ports and Services
Netskope recommends that you configure these ports and services for HA configurations:
Port 80/443: Cloud Exchange UI
Port 4369: A peer discovery service used by RabbitMQ nodes and CLI tools
Port 5672: Used by AMQP 0-9-1 and AMQP 1.0 clients without and with TLS
Port 15672: HTTP API clients, management UI and rabbitmqadmin, without and with TLS
Port 25672: Used for inter-node and CLI tools communication
Port 35672: Used for inter-node and CLI tools communication
Port 27017: The default port for mongodb and mongos instances.
Storage
Cloud Exchange uses NFS for shared storage, so it is important that you configure the NFS volume in a manner that restricts access exclusively to Netskope CE instances. This precaution is of utmost importance in order to strengthen security measures.
Cloud Exchange Hardening
Netskope provides these options to securely configure the Cloud Exchange post deployment.
Credentials and Secret Management
By default, credentials required for all Cloud Exchange operations are stored within a password-protected MongoDB. The data stored within Mongo is unencrypted.
Note that data encryption within Mongo is available in the Enterprise edition.
Secrets Manager can be used to allow users to configure Netskope tenant, customer plugin repositories, and plugins using secrets from their configured
Secrets Manager
. When configured, only the secrets paths will be stored in MongoDB.
Currently available options for Secrets Manager:
Hashicorp Vault
Perform these steps as a user with write privileges:
Go to
Settings > General > Secret Manager
.
By default, the Secrets Manager is disabled. Enable the
Secrets Manager
toggle.
Leave the default value for the Secrets Manager. Hashicorp is currently the only option.
Provide the Vault URL and Namespace.
Select an authentication method. Currently supported authentication methods are:
Token (
https://developer.hashicorp.com/vault/docs/auth/token
)
AppRole (
https://developer.hashicorp.com/vault/docs/auth/approle
)
Username & Password (
https://developer.hashicorp.com/vault/docs/auth/userpass
)
Provide the required parameters for the selected authentication method and click
Save
.
Secrets Management
Configure these Tenant settings to manage the secrets used for custom plugin repositories or Netskope Tenants with Secret Manager.
You still have the option to directly provide the password value instead of the secret path by disabling the toggle.
Ports and Services
Ensure only below ports are enabled and the associated services are running on those ports:
Port: 80/443 HTTP/HTTPS
Configurable – during the setup
Used to access CE UI
Port: 15672
Configurable – No
Used for RabbitMQ dashboard
Communication Security
Cloud Exchange provides an option to configure TLS 1.3 and/or TLS1.2 during setup. These are used for security of the communication channel for the Cloud Exchange UI.
Cloud Exchange generates a self-signed certificate to use for any of the protocols. Netskope recommends using a CA-signed certificate for this. Cloud Exchange provides an option to upload your certificates.
For more detailed information on how to manage certificates, go
here
.
User Management
Cloud Exchange comes with three default local users. All three users have different roles associated. Netskope recommends configuring these users as per requirement, and changing the default password for these users after configurations and setup.
Here are the users and their roles:
admin: Used to access the Cloud Exchange UI.
user: Used to access the RabbitMQ dashboard.
cteadmin: Used to access the mongo database.
After supporting local user accounts, Cloud Exchange also supports provisioning of users via SSO. Provisioning users via SSO provides more security and is recommended. Refer to the documentation
here
.
Password Policy
Although Cloud Exchange does not enforce a strict password policy, it is recommended to use a strong password with these options:
Password must contain at least one lower case letter
Password must contain at least one uppercase letter
Password must contain at least one special character (e.g #, @,)
Password must contain at least one numeric character
Minimum 8 characters are required for the password
Maximum 72 characters are supported for the password
Updates and Upgrades
Netskope releases updates and upgrades for Cloud Exchange regularly to improve the functionality of the product, and also address the security issues and gaps in the product. We recommend that you keep the Cloud Exchange updated with the latest version provided by Netskope.
For more detailed information, go
here
.
In this Topic
Secure Tenant Configuration and Hardening

---
## Delete or Downgrade the Global Administrator Account
**URL:** https://docs.netskope.com/en/delete-or-downgrade-the-global-administrator-account-326348/
**Last Modified:** 2025-08-31T01:41:20+00:00
**Scraped:** 2026-08-02T08:22:39.741664+00:00

Delete or Downgrade the Global Administrator Account - Netskope Knowledge Portal
Delete or Downgrade the Global Administrator Account
Netskope requires a global administrator account to grant rights to the Netskope Activity Feeds for Microsoft Office 365 Teams application. Post-grant, you can delete or downgrade the original service account that you have used to set up the Microsoft Office 365 Teams app instance. To do so, follow the steps below:
Log in to the Netskope tenant and navigate to
Settings > Configure App Access > Classic > SaaS
and click the Microsoft Office Teams app.
The UI displays a list of app instances.
Click the relevant app instance and note down the admin email address.
Log in to the Microsoft Office 365 admin center at
login.microsoftonline.com
.
Note
Do not log in with the global administrator email account that you have used to set up the Microsoft Office 365 Teams app instance. You should log in using an alternate administrator account. Ensure that the logged in user has enough permissions to delete or downgrade a global administrator role. For example, you can log in as a user administrator account.
Navigate to
Admin > Users > Active users
. Search for the user you noted in step 2 and select the user.
Under the
Accounts
tab, you can either delete the user or downgrade the role:
To delete the user, click
Delete user
.
Note
If you intend to re-grant the Microsoft Office 365 Teams app instance anytime in future, create a temporary user with a global administrator role and use this account to re-grant.
To downgrade the role, under
Roles
, click
Manage roles
. Select a non-global administrator role and click
Save changes
.
Note
If you intend to re-grant the Microsoft Office 365 Teams app instance anytime in future, reassign the global administrator role to the user before re-granting.
Important
If you intend to integrate Microsoft Information Protection (MIP) with Netskope, you should downgrade the admin role to
Azure Information Protection Administrator
and
Application Administrator
at a minimum.
In this Topic
Delete or Downgrade the Global Administrator Account

---
## Delete or Downgrade the Global Administrator Account
**URL:** https://docs.netskope.com/en/delete-or-downgrade-the-global-administrator-account-326337/
**Last Modified:** 2025-09-01T12:34:07+00:00
**Scraped:** 2026-08-02T08:22:42.121461+00:00

Delete or Downgrade the Global Administrator Account - Netskope Knowledge Portal
Delete or Downgrade the Global Administrator Account
Netskope requires a global administrator account to grant rights to the Netskope Activity Feeds for Microsoft Office 365 SharePoint Sites application. Post-grant, you can delete or downgrade the original service account that you have used to set up the Microsoft Office 365 SharePoint Sites app instance. To do so, follow the steps below:
Log in to the Netskope tenant and navigate to
Settings > Configure App Access > Classic > SaaS
and click the Microsoft Office SharePoint Sites app.
The UI displays a list of app instances.
Click the relevant app instance and note down the admin email address.
Log in to the Microsoft Office 365 admin center at
login.microsoftonline.com
.
Note
Do not log in with the global administrator email account that you have used to set up the Microsoft Office 365 SharePoint Sites app instance. You should log in using an alternate administrator account. Ensure that the logged in user has enough permissions to delete or downgrade a global administrator role. For example, you can log in as a user administrator account.
Navigate to
Admin > Users > Active users
. Search for the user you noted in step 2 and select the user.
Under the
Accounts
tab, you can either delete the user or downgrade the role:
To delete the user, click
Delete user
.
Note
If you intend to re-grant the Microsoft Office 365 SharePoint Sites app instance anytime in future, create a temporary user with a global administrator role and use this account to re-grant.
To downgrade the role, under
Roles
, click
Manage roles
. Select a non-global administrator role and click
Save changes
.
Note
If you intend to re-grant the Microsoft Office 365 SharePoint Sites app instance anytime in future, reassign the global administrator role to the user before re-granting.
Important
If you intend to integrate Microsoft Information Protection (MIP) with Netskope, you should downgrade the admin role to
Azure Information Protection Administrator
and
Application Administrator
at a minimum.
In this Topic
Delete or Downgrade the Global Administrator Account

---
## Delete or Downgrade the Global Administrator Account
**URL:** https://docs.netskope.com/en/delete-or-downgrade-the-global-administrator-account/
**Last Modified:** 2025-09-01T12:34:10+00:00
**Scraped:** 2026-08-02T08:22:43.306425+00:00

Delete or Downgrade the Global Administrator Account - Netskope Knowledge Portal
Delete or Downgrade the Global Administrator Account
Netskope requires a global administrator account to grant rights to the Netskope Activity Feeds for Microsoft Office 365 OneDrive for Business application. Post-grant, you can delete or downgrade the original service account that you have used to set up the Microsoft Office 365 OneDrive for Business app instance. To do so, follow the steps below:
Log in to the Netskope tenant and navigate to
Settings > Configure App Access > Classic > SaaS
and click the Microsoft Office OneDrive for Business app.
The UI displays a list of app instances.
Click the relevant app instance and note down the admin email address.
Log in to the Microsoft Office 365 admin center at
login.microsoftonline.com
.
Note
Do not log in with the global administrator email account that you have used to set up the Microsoft Office 365 OneDrive for Business app instance. You should log in using an alternate administrator account. Ensure that the logged in user has enough permissions to delete or downgrade a global administrator role. For example, you can log in as a user administrator account.
Navigate to
Admin > Users > Active users
. Search for the user you noted in step 2 and select the user.
Under the
Accounts
tab, you can either delete the user or downgrade the role:
To delete the user, click
Delete user
.
Note
If you intend to re-grant the Microsoft Office 365 OneDrive for Business app instance anytime in future, create a temporary user with a global administrator role and use this account to re-grant.
To downgrade the role, under
Roles
, click
Manage roles
. Select a non-global administrator role and click
Save changes
.
Note
If you intend to re-grant the Microsoft Office 365 OneDrive for Business app instance anytime in future, reassign the global administrator role to the user before re-granting.
Important
If you intend to integrate Microsoft Information Protection (MIP) with Netskope, you should downgrade the admin role to
Azure Information Protection Administrator
and
Application Administrator
at a minimum.
In this Topic
Delete or Downgrade the Global Administrator Account

---
## Deleting AWS Instances in the Netskope Tenant
**URL:** https://docs.netskope.com/en/deleting-aws-instances-in-the-netskope-tenant/
**Last Modified:** 2025-08-31T01:46:32+00:00
**Scraped:** 2026-08-02T08:22:56.201300+00:00

Deleting AWS Instances in the Netskope Tenant - Netskope Knowledge Portal
Deleting AWS Instances in the Netskope Tenant
To delete AWS accounts in the Netskope tenant from the from AWS Management Console,
Log into the AWS Management Console using the credentials of the AWS account you want to delete from the Netskope tenant and navigate to
Services > CloudFormation
.
Select the stack created using
add_accounts_cft.yml
and click
Delete
.
In this Topic
Deleting AWS Instances in the Netskope Tenant

---
## Step 3/3: Add the Azure Subscription to the Netskope tenant for CSA
**URL:** https://docs.netskope.com/en/step-3-3-add-the-azure-subscription-to-the-netskope-tenant-for-csa/
**Last Modified:** 2025-08-31T01:46:02+00:00
**Scraped:** 2026-08-02T08:28:21.824899+00:00

Step 3/3: Add the Azure Subscription to the Netskope tenant for CSA - Netskope Knowledge Portal
Step 3/3: Add the Azure Subscription to the Netskope tenant for CSA
Once you have created an Microsoft Entra ID application and assigned the relevant permissions/roles, you can now create an Azure app instance in the Netskope UI.
To create an Azure instance:
Log in to the Netskope tenant UI.
Navigate to
Microsoft Azure > Setup
. The
New Setup
window opens.
In the
New Setup
window, enter the following parameters:
In the
Azure Subscription
sector, enter the following details:
Azure Subscription Name: Enter a unique name for the Azure subscription.
Admin Email: Enter the email address of the administrator for email notification.
Connection Type: Select
Security Posture
. Security Posture periodically assesses the configuration of the Azure services to monitor risks in your infrastructure. You have the option to run the policy at intervals (30 minutes, 60 minutes, 2 hours, 6 hours, and 24 hours). On selecting this option, you need to create a security assessment policy.
Netskope recommends setting the interval to 60 minutes or more.
Few of the instance type options may be disabled. Contact your Netskope sales representative for additional information.
In the
Cloud Provider Information
section, enter the following details:
Directory ID: Enter the Directory ID you noted from
Get the Application ID and Directory ID
section in
Step 1/3: Configure a Microsoft Entra ID Application for CSA
Application ID: Enter the Application ID you noted from
Get the Application ID and Directory ID
section in
Step 1/3: Configure a Microsoft Entra ID Application for CSA
Client Key: Enter the authentication key you noted from
Get the Application ID and Directory ID
section in
Step 1/3: Configure a Microsoft Entra ID Application for CSA
Click
Save
, then click
Grant Access
for the Azure instance you just created.
Refresh your browser, and you should see a green check icon next to the instance name. You can proceed to create a security assessment policy.
To learn more:
Creating Security Assessment Policies for Netskope Public Cloud Security
.
You can view detailed information about all the events and scan results under
API-enabled Protection > Compliance > Security Posture
. To learn more:
View Security Posture Compliance
.
In this Topic
Step 3/3: Add the Azure Subscription to the Netskope tenant for CSA

---
## Step 3/3: Set up a Netskope instance with Azure App Registration credentials
**URL:** https://docs.netskope.com/en/step-3-3-add-the-azure-subscription-to-the-netskope-tenant-for-forensics/
**Last Modified:** 2025-08-31T01:46:26+00:00
**Scraped:** 2026-08-02T08:28:24.100428+00:00

Step 3/3: Set up a Netskope instance with Azure App Registration credentials - Netskope Knowledge Portal
Step 3/3: Set up a Netskope instance with Azure App Registration credentials
Once you have created an Microsoft Entra ID application and assigned the relevant permissions/roles, you can now create an Azure app instance in the Netskope UI.
To create an Azure instance:
Log in to the Netskope tenant UI.
Navigate to
Settings > Configure App Access > Classic > IaaS
> Microsoft Azure > SETUP
.
The
New Setup
window opens.
In the
New Setup
window, enter the following parameters:
In the
Netskope Instance
section, enter the following details:
Instance Name: Enter a unique name for the Netskope Instance.
Admin Email: Enter the email address of the administrator for email notification.
Connection Type: Select
Forensic
.
Few of the instance type options may be disabled. Contact your Netskope sales representative for additional information.
In the
Azure App Registration Credentials
section, enter the following details:
Directory ID: Enter the directory ID you noted from
Get the Application ID and Directory ID
section in
Step 1/3: Configure a Microsoft Entra ID Application for Forensics
.
Application ID: Enter the application ID you noted from
Get the Application ID and Directory ID
section in
Step 1/3: Configure a Microsoft Entra ID Application for Forensics
.
Client Key: Enter the authentication key you noted from
Get the Authentication Key
section in
Step 1/3: Configure a Microsoft Entra ID Application for Forensics
.
Click
Save
, then click
Grant Access
for the Azure instance you just created.
Refresh your browser, and you should see a green check icon next to the instance name.
Once you set up the instance with forensic enabled, you should create a forensic profile. To learn more:
Creating a Forensic Profile for Public Cloud Storage
.
For frequently asked questions on regranting of Azure instances, refer to
Azure forensics Instance Re-grant FAQs
In this Topic
Step 3/3: Set up a Netskope instance with Azure App Registration credentials

---
## Step 4/4: Add the Azure Subscription to the Netskope Tenant for Data Protection
**URL:** https://docs.netskope.com/en/step-4-4-add-the-azure-subscription-to-the-netskope-tenant-for-data-protection/
**Last Modified:** 2025-08-31T01:46:14+00:00
**Scraped:** 2026-08-02T08:28:25.211299+00:00

Step 4/4: Add the Azure Subscription to the Netskope Tenant for Data Protection - Netskope Knowledge Portal
Step 4/4: Add the Azure Subscription to the Netskope Tenant for Data Protection
Once you have created an Microsoft Entra ID application and assigned the relevant permissions/roles, you can now create an Azure app instance in the Netskope UI.
If you wish to set up the instance in Azure US Government Cloud, please contact your Technical Account Manager to request enablement for your tenant, before proceeding.
Please note, if you are switching from using Azure Public to Azure Government (or vice-versa), any existing Azure instances must be deleted before switching over.
To create an Azure instance:
Log in to the Netskope tenant UI.
Navigate to
Settings > Configure App Access > Classic > IaaS
> Microsoft Azure > SETUP
.
The
New Setup
window opens.
In the
New Setup
window, enter the following parameters:
In the
Azure Subscription
section, enter the following details:
Azure Subscription Name: Enter a unique name for the Azure subscription.Admin Email: Enter the email address of the administrator for email notification.Connection Type: Select
DLP Scan
and
Threat Protection (Malware Scan)
.
DLP scanning requires DLP policies to perform scans. To learn more:
Create an API Data Protection Policy
.Malware scanning requires Threat Protection policies to perform scans. To learn more:
Create an API Data Protection Policy
.
Note
Few of the instance type options may be disabled. Contact your Netskope sales representative for additional information.
In the
Cloud Provider Information
section, enter the following details:
Directory ID: Enter the directory ID you noted from
Get the Application ID and Directory ID
section in
Step 2/4: Configure a Microsoft Entra ID Application for Data Protection
.Application ID: Enter the application ID you noted from
Get the Application ID and Directory ID
section in
Step 2/4: Configure a Microsoft Entra ID Application for Data Protection
.Client Key: Enter the authentication key you noted from
Get the Authentication Key
section in
Step 2/4: Configure a Microsoft Entra ID Application for Data Protection
.
Click
Save
, then click
Grant Access
for the Azure instance you just created.
Refresh your browser, and you should see a green check icon next to the instance name. You can proceed to create API Data Protection policies.
To learn more:
Creating Data Protection Policies for Netskope Public Cloud Security
.
You can view detailed information about alerts in the
Skope IT > Alerts
pages. To learn more:
Viewing DLP and Malware Alerts for Public Cloud Storage
In this Topic
Step 4/4: Add the Azure Subscription to the Netskope Tenant for Data Protection

---
## Upload Logs to the Netskope Tenant UI
**URL:** https://docs.netskope.com/en/upload-logs-to-the-netskope-tenant-ui/
**Last Modified:** 2025-08-31T01:50:03+00:00
**Scraped:** 2026-08-02T08:28:56.593197+00:00

Upload Logs to the Netskope Tenant UI
You can upload the log files from your log source to the Netskope UI. For logs greater than 1000 MB in size, we recommend using the SFTP to upload logs. Refer to the subsequent sections for uploading logs using SFTP on Windows and Mac/Linux.
Note
Binary format is not supported.
Login to the tenant UI. Go to
Settings > Risk Insights > Log > Upload
, and click
Upload Logs
.
Click
Select File
, and go to and select the log file.
Choose the type of the log file. For example, if you are uploading a checkpoint log, choose the log type as
chkp
.
Click
Upload
to upload the log.
In this Topic
Upload Logs to the Netskope Tenant UI

---
## Operating Cloud Exchange
**URL:** https://docs.netskope.com/en/cloud-exchange-console/
**Last Modified:** 2026-03-21T01:18:36+00:00
**Scraped:** 2026-08-02T08:31:23.076226+00:00

Operating Cloud Exchange - Netskope Knowledge Portal
Operating Cloud Exchange
Only Admins can manage certain Settings. This section provides details about the different pages and configurations for the Cloud Exchange platform. For details about the contents on the Home page, go to
Explore the Dashboards
.
Password Policy
Cloud Exchange KB Articles
Cloud Exchange High Availability
Migrate Cloud Exchange Fargate to AMI EC2 VM
Cloud Exchange Sizing using Netskope Advanced Analytics
Update Cloud Exchange Plugins
Settings
API Tokens
Cloud Exchange Users
Plugin Store
Plugin Repository
Logging
Help
Tasks
Account Settings
Monitor Cloud Exchange with Prometheus and Grafana
Cloud Exchange FAQs
Cloud Exchange Troubleshooting
In this Topic
Operating Cloud Exchange

---
## Create a File Profile in your Netskope Tenant for File Hashes
**URL:** https://docs.netskope.com/en/create-a-file-profile-in-your-netskope-tenant-for-file-hashes/
**Last Modified:** 2025-11-01T00:42:02+00:00
**Scraped:** 2026-08-02T08:32:08.048793+00:00

Create a File Profile in your Netskope Tenant for File Hashes - Netskope Knowledge Portal
Create a File Profile in your Netskope Tenant for File Hashes
The Netskope tenant can not receive information from Threat Exchange via RESTful API commands until a file has been created in the Netskope tenant.
In your Netskope tenant, go to
Policies > Profiles > File
.
Click
New File Profile
Select
File Hash
and from the dropdown select the type(s) you are going to be sending to Netskope.
You can select both of them in the same file name. Selecting both means Netskope will be able to leverage both kinds of file hashes sent from Threat Exchange to the same file for use in the same malware detection policy (which only supports a single custom file).
Click
Next
Add a Profile Name and click
Save
Note
This profile name must exactly match the name you use in Threat Exchange (case-sensitive).
In this Topic
Create a File Profile in your Netskope Tenant for File Hashes

---
## Admin Account Domains
**URL:** https://docs.netskope.com/en/admin-account-domains/
**Last Modified:** 2025-08-31T01:38:42+00:00
**Scraped:** 2026-08-02T08:35:25.526830+00:00

Admin Account Domains - Netskope Knowledge Portal
Admin Account Domains
Admin accounts can only be created from the domains your Netskope admin specifies in the Admin Domains list below. This applies for both RBAC V1 and V2.
PREREQUISITES
You must first ensure any new admins you create have email addresses with domains added here in your Admin Account Domains list. To learn more:
Create Administrators
Ensure the domains used for SSO/SLO Settings have email addresses with domains added here in your Admin Account Domains list. To learn more:
SSO Settings
Existing user domains are automatically imported by the system during set-up. Therefore you may see some domains pre-populated in your Admin Account Domains list.
To define an admin account domain, follow the steps below:
Navigate to
Settings
>
Administration
>
Internal Domains
.
Click
Edit
and enter the domains. Enter one domain name per line. You can use wild card (*), for example, *.example.*. In addition, if you add “*.domain.com” in the Admin Account Domains, then any admin with domains like test.domain.com, test.newdomain.domain.com is allowed.
Supported formats:
*.domain.com (can be any length after *. ) e.g., test1.domain.com, test2.domain.com
domain.test.* (can be any length before .* ) e.g., domain.test.com, domain.test.br
domain.*.com (can be any length before and after .*. ) e.g., domain.domain2.com, domain.domain3.com
*.test.domain.* (can be any length between *. and .* ) e.g., domain.test.domain.com, domain-test.test.domain.ac.in
Click
Save
.
You must configure at least one Admin Account Domain or the following coaching message appears on your dashboard page.
AUDIT LOG
Navigate to
Settings
>
Administration
>
Audit Log
to view activity details for users.
The ‘Activity’ column shows general activity such as log in info, log out info, and upon account creation the admin role assigned to the new account, etc.
Click Activity column >
View Details
to see more details regarding the changes made by the admin. Details include the admin account that changed the settings, the before and after setting change, etc.
RBAC PRIVILEGES
Navigate to
Settings
>
Administration
>
Roles
to ensure admins have the correct privilege level. The following applies to both RBAC V1 and V2:
Users with “None” permissions will not see the Internal Domains page.
Users with “View” or “View Only” permissions will be able to view the Internal Domains page but cannot edit the Admin Account Domains or Internal Domains sections.
If you migrate from RBAC V1 to RBAC V2, permissions for the Admin and Internal Domains remains unchanged for all the custom roles. This is done by the system migration automatically.
If you are currently running RBAC V2, the Internal Domains are added to your custom and pre-defined roles with the permissions matching the Administration page settings. This is done by the system migration automatically.
Existing Next Gen CASB API users using custom roles must manually update the Internal Domains page access settings in the respective RBAC custom roles.
RBAC V1: Administrators must have “View and Manage” enabled.
RBAC V2: Administrators must have Page Permissions > Settings > Administration > Internal Domains > Manage enabled.
In this Topic
Admin Account Domains

---
## Administration
**URL:** https://docs.netskope.com/en/administration/
**Last Modified:** 2025-08-31T01:38:34+00:00
**Scraped:** 2026-08-02T08:35:26.641828+00:00

Administration - Netskope Knowledge Portal
Administration
As an administrator, you have access to your tenant instance in Netskope. The Netskope UI provides full access to deploying and managing the Netskope solution. There are several administrator account types. You can assign each admin a specific role which has different admin privileges. You can configure an admin user as one of the admin account types. In addition, you can create custom designed roles based on your business needs.
Log in to your tenant instance in Netskope using the URL provided in the initial onboarding email sent from Netskope. Upon first log in, you will be prompted to change the admin password.
Begin with creating accounts for access to the Netskope tenant. There are various roles and privilege associated with each role. You can also create custom roles for specific privileges. A Tenant Admin can also configure functions like SSO, log in attempts, idle timeout periods, password expiration, and more.
Audit Log
Licenses
Telemetry
CASB API Usage
SSO for Administrators
Managing Administrators
Managing Administrators for RBAC V3
Managing Administrators for RBAC V2
Certificates
Privacy Notice
Set Log In Attempts
Set Idle Timeout
IP Allowlisting
Disallow Concurrent Logins by an Admin
Set Password Expiration
Change Access for an Admin Account
In this Topic
Administration

---
## Admins Settings Page
**URL:** https://docs.netskope.com/en/admins-settings-page/
**Last Modified:** 2025-08-31T01:38:48+00:00
**Scraped:** 2026-08-02T08:35:28.858464+00:00

Admins Settings Page - Netskope Knowledge Portal
Admins Settings Page
The Admins Settings page contains general functions that apply to all admins.
On the Settings page (
Settings
>
Administration
>
Admins
>
Settings
icon) you can:
Set Log In Attempts
Set Idle Timeout
Set Password Expiration
Disallow concurrent log ins by the same admin. This means if an admin logs in from a second browser instance, they will be logged out from their first browser session.
In this Topic
Admins Settings Page

---
## Assign Roles to Restricted Administrators
**URL:** https://docs.netskope.com/en/assign-roles-to-restricted-administrators/
**Last Modified:** 2025-08-31T01:38:41+00:00
**Scraped:** 2026-08-02T08:35:41.181909+00:00

Assign Roles to Restricted Administrators - Netskope Knowledge Portal
Assign Roles to Restricted Administrators
To assign roles to a restricted admin:
Go to
Settings > Administration > Admins
.
Click
New Admin
.
Specify the email address (username) and password, or choose to generate a password automatically. If you create a password, note the password requirements.
Set the admin account type as Restricted Admin.
Assign a role for the user.
Click
Create
to add the new admin.
The new admin will be prompted to change the password upon first log in. You can delete the admin user or role at any time.
In this Topic
Assign Roles to Restricted Administrators

---
## Change Access for an Admin Account
**URL:** https://docs.netskope.com/en/change-access-for-an-admin-account/
**Last Modified:** 2026-02-20T00:17:03+00:00
**Scraped:** 2026-08-02T08:35:44.537400+00:00

Change Access for an Admin Account - Netskope Knowledge Portal
Change Access for an Admin Account
The tenant admin can enable, disable, and delete other admin accounts. For example:
If an admin gets locked out of the UI, you can restore access.
If an admin is no longer active, you can disable or delete the admin account.
To enable or disable an admin:
Go to
Settings > Administration > Administrators & Roles
.
To enable an admin that has a
Disabled
Status, click the
button for the admin and select
Enable
.
To disable an admin that has an
Enabled
Status, click the
button for the admin and select
Disable
.
To decommission an admin (permanently delete an admin account):
Go to
Settings > Administration > Administrators & Roles
.
Click the
button for the admin and select
Delete
.
In this Topic
Change Access for an Admin Account

---
## Create Administrators
**URL:** https://docs.netskope.com/en/create-administrators/
**Last Modified:** 2025-08-31T01:38:40+00:00
**Scraped:** 2026-08-02T08:36:07.866785+00:00

Create Administrators - Netskope Knowledge Portal
Create Administrators
Login to the Netskope tenant UI as the tenant administrator. The default tenant admin username is nsadmin.
To create a delegated admin:
Go to
Settings > Administration > Admins
.
Click
New Admin
.
Enter an email address (username) and for password, choose to generate a password automatically or create one. If you create a password, note the password requirements:
8+ characters
A mix of lower/upper case, numbers, and symbols
Select the radio button for how to provide the password for the new admin. Note the username and password if you opt to manually provide the password. Note the password restrictions for the admin user. If you use the default selection to generate a new password, the administrator is prompted to change the password upon first log in. You can delete the admin user any time.
Select the role to assign the new admin. Your choices include:
Tenant Admin: Top level admin that has all privileges.
Delegated Admin: All privileges except managing other admins.
Restricted Admin: Has read-only access to all functions.
Cloud Intelligence Analyst: Has access only to reporting and analytics.
Application Risk Analyst: Can run reports and analytics and read the CCI.
Enterprise Applications Admin: Can manage the application CCI.
Directory Admin: Can manage users.
Security Admin: Can manage settings.
InfoSec Operations Admin: Can manage policies.
Compliance Officer: Can remediate DLP incidents.
Security Analyst: Can analyze malware and threat.
For more details about access privileges for each of these roles, refer to
Managing Administrators
.
Click
Create
to notify the new admin.
In this Topic
Create Administrators

---
## Create Admins and Assign to Roles
**URL:** https://docs.netskope.com/en/create-admins-and-assign-to-roles/
**Last Modified:** 2025-08-31T01:38:50+00:00
**Scraped:** 2026-08-02T08:36:12.297474+00:00

Create Admins and Assign to Roles - Netskope Knowledge Portal
Create Admins and Assign to Roles
The process of creating an admin by assigning a role ensures that rules and settings configured by that admin aren’t impacted even if the admin account is modified or deleted at some point in the future. This is because the settings are associated with an admin’s role (which is defined by privileges, scope, and file) rather than a particular admin.
In addition, if an admin account is deleted, you don’t lose all the distinct permissions associated with that admin. You can simply reassign the admin role to another admin.
For example, your organization’s CISO may have an admin account with access to all security-related policies and scope over the organization. If that CISO leaves the organization and his account is deleted, the policy rules he created would not be affected and would remain in place. In addition, you can easily assign the next CISO the same role as the previous CISO, without redefining permissions from scratch.
With role-based administration, you can easily add admins and assign them specific roles, with differing levels of access to the Netskope platform.
Note
Based on your role, you can only edit admin roles of the same or admin roles with fewer privileges than yourself.
To create an admin and assign to a role:
Navigate to
Settings
>
Administration
>
Admins
.
Click
New Admin
.
Type the admin’s email address.
Select the admin’s role. You must create the role first before it appears in this dropdown list. To learn more:
Create Roles
Select the option to generate a password, choose to generate a password automatically or create one. If you create a password, note the password requirements:
8+ characters
A mix of lower/upper case, numbers, and symbols
Click
Save
.
In this Topic
Create Admins and Assign to Roles

---
## Create Roles for Restricted Administrators
**URL:** https://docs.netskope.com/en/create-roles-for-restricted-administrators/
**Last Modified:** 2025-08-31T01:38:40+00:00
**Scraped:** 2026-08-02T08:36:23.310049+00:00

Create Roles for Restricted Administrators - Netskope Knowledge Portal
Create Roles for Restricted Administrators
To create roles for a restricted admin:
Go to
Settings > Administration > Roles
.
Click
Create New
.
Provide a Role name, and description if desired. The role type is set to Read Only by default.
Specify the list of users and/or groups the admin will have access to.
Allow access to file content, this allows admins to download, preview, and view files from API-enabled Protection and Forensics.
Optionally, you can choose the option to obfuscate none or specific fields. Obfuscate is a form of data masking for security reasons. Enable this to hide sensitive data in the UI. This only applies to Events, API-enabled Protection, Reports, Forensics, and Malware functional areas.
In the example above, the IT group is chosen. The IT group is the Active Directory Group exported to the tenant instance in the Netskope cloud using AD Importer. You can also choose individual users. Other options include:
Obfuscate None: If you choose this option, restricted admins who are assigned this role can see sensitive data such as username, source IP, etc.
Specific Fields: Select this option to mask the following information from users: User names and IPs, Source location information, File and object names, App names, URLs, and Dest IPs.
Scope: If you choose a specific list of Users, Groups, or App Instances under Scope, a restricted admin who is assigned this role can only view the data pertaining to those users or the specific Active Directory group, like viewing cloud apps usage for these users, creating reports for these users, etc. Restricted admins cannot view data of other users who are not part of this group.
Note
Users and groups can be automatically populated from the Microsoft Active Directory. This requires an AD Importer to be installed on the AD server, or a member server that can export the AD usernames and group names to your tenant instance in the Netskope cloud.
Select Scope, All events or select specific events. Selecting this option restricts the scope of data shown in the UI. This only applies to Events, Reports, Forensics, and Malware functional areas.
Click
Create
.
Now you can assign a role to a restricted admin.
In this Topic
Create Roles for Restricted Administrators

---
## Disallow Concurrent Logins by an Admin
**URL:** https://docs.netskope.com/en/disallow-concurrent-logins-by-an-admin/
**Last Modified:** 2025-08-31T01:38:54+00:00
**Scraped:** 2026-08-02T08:36:41.666296+00:00

Disallow Concurrent Logins by an Admin - Netskope Knowledge Portal
Disallow Concurrent Logins by an Admin
You can ensure that an admin can log in to a tenant only once, instead of being able to log in to a tenant multiple times concurrently. The default setting currently allows concurrent logins.
To disallow concurrent logins:
To change the default, go to
Settings > Administration > Admins
.
On the top right-hand side, click the Tools icon to open the Configure dialog box. Activate
Disallow Concurrent Logins by same Admin
.
Click
Save
.
In this Topic
Disallow Concurrent Logins by an Admin

---
## Manage Administrators
**URL:** https://docs.netskope.com/en/manage-administrators/
**Last Modified:** 2025-08-31T01:38:47+00:00
**Scraped:** 2026-08-02T08:37:26.165235+00:00

Manage Administrators - Netskope Knowledge Portal
Manage Administrators
The Netskope UI provides full access for deploying and managing admin rights for the Netskope solution. Netskope’s role-based administration enables you to control what different admins can do in the solution. You can delegate responsibilities among admins and granularly control their level of access to the solution to ensure they do not create conflicting policies and settings.
The high level workflow for implementing role-based administration includes:
creating Real-time Protection Policy groups
creating new roles
creating admins and assigning them to roles
On the Settings > Administration > Admins page, you can do the following:
Add a
new admin
.
View the
Settings
dialog box.
View a list of all admins configured for your organization. For each admin, you can see the following:
Enabled: shows the status of the admin. Click the slider to enable/disable the admin.
Email: the Netskope log in ID for the admin.
Type: displays the admin’s type of role as a Super Admin, Manager Admin, or Regular Admin.
Role: the admin’s level of access to the functional areas, page permissions, and file access. This is the role chosen which can be a predefined or custom role.
Enable or disable an admin. Click the slider to enable/disable the admin.
Delete or edit an admin.
In this Topic
Manage Administrators

---
## Multi-Factor Authentication for Netskope Admins
**URL:** https://docs.netskope.com/en/multi-factor-authentication-for-netskope-admins/
**Last Modified:** 2025-10-09T23:38:08+00:00
**Scraped:** 2026-08-02T08:37:32.755486+00:00

Multi-Factor Authentication for Netskope Admins - Netskope Knowledge Portal
Multi-Factor Authentication for Netskope Admins
Creating Netskope Local Admin Accounts
Most enterprise accounts implement Netskope SSO for management console access. In addition, local accounts are created for emergency access for a variety of business use cases. Multi-factor authentication (MFA) enhances the security of the user log in process by requiring users to provide unique authentication in addition to their regular sign in.
The Netskope platform supports MFA for Netskope admins to log in to the Netskope management console using a local administrator account.
Navigate to
Settings
>
Administration
>
Admins
to view the Admins page.
Any Local Account type can be enabled for MFA.
MFA Status column lists the user status: Enabled, Disabled, Pending Registration (user action required).
Click
ellipses
>
Edit
to enable, delete, or reset MFA for a local admin user (requires user to authenticate with email and OTP).
Creating Netskope Local Account Admins
You can create a new admin and enable multi-factor authentication (MFA) for the user (Local Account type only). This is helpful so users cannot reuse/share login credentials.
Navigate to
Settings
>
Administration
>
Admins
to view the Admins page.
Click
New Admin
.
Select a role.
Optionally, enable the
MFA toggle
. To learn more:
Enabling MFA for Netskope Local Accounts
Click
Save
.
Admins List Page
View the Admins List page. You will see the new admin email listed with an orange icon. This icon indicates that this account still needs to be verified. It is enabled once verification is complete.
To complete account verification, Netskope sends two emails to the user. One with an account activation URL.
After the user clicks
Activate Account
, a second email with a one-time password (OTP) is sent.
The new admin user must click the link to verify their email which consists of changing their temporary password and entering the OTP.
Resend Verification Email
If the user does not receive the email verification or the link expires, click the
Resend Verification Email
to send a new link.
You can click
Resend Verification Email
from the orange icon next to the admin’s name.
Optionally, navigate to the admin’s name in the
Admins
list page > click the
ellipses
at the end of the row > click
Resend Verification Email
.
The Resend Verification Email or Reset Password function inactivates the account and requires re-verification. Netskope will send a verification email to the user to re-activate the account. The account will be re-enabled once the user completes account verification.
Verification Time Period
Navigate to
Admins
>
Settings
to configure the local account verification period. Users will receive a verification link via email when their admin account is created or password is reset for a local account. You can define how long the verification link is valid. The minimum is 15 minutes and the maximum is 72 hours. The default time period is 24 hours.
Enabling MFA for Netskope Local Accounts
Click ellipses at the end of the local admin account user. The Edit Admin page displays.
Toggle the Multi-Factor Auth radio button from “Disabled” (default) to “Enabled”.
The next time the local admin logs in to their account, the admin must re-verify their account. Emails are sent to the email associated with the admin’s Netskope account. To learn more:
Admins List Page
Audit Log
Navigate to
Settings
>
Administration
>
Audit Lo
g to view MFA local account user activity.
In this Topic
Multi-Factor Authentication for Netskope Admins

---
## Managing Administrators
**URL:** https://docs.netskope.com/en/managing-administrators/
**Last Modified:** 2026-07-31T04:30:08+00:00
**Scraped:** 2026-08-02T08:37:36.114372+00:00

Managing Administrators - Netskope Knowledge Portal
Managing Administrators
The Netskope UI provides full access for deploying and managing admin rights for the Netskope solution.  As a Tenant Admin, you have full privileges to create and manage other admins.
Summary of Operations by Predefined Roles and Privileges
View and Manage means admins with this designation can perform all actions. View Only means admins with this designation can view, export CSV files, and download and email PDFs.
Privilege/Role
Iaas/PaaS
Admins
Advanced Settings
Settings
CCI
Events
Tenant Admin
View and Manage
View and Manage
View and Manage
View and Manage
View and Manage
View and Manage
Delegated Admin
View and Manage
View and Manage
View and Manage
View and Manage
Restricted Admin
View Only
View Only
Cloud Intelligence Analyst
Application Risk Analyst
View Only
Enterprise Applications Admin
View and Manage
Directory Admin
View Only
View Only
Security Admin
View and Manage
View and Manage
View and Manage
View and Manage
InfoSec Operations Admin
View and Manage
View and Manage
Compliance Office
View and Manage
Security Analyst
View and Manage
View Only
Iaas/PaaS
View and Manage
View and Manage
View and Manage
NS Technical Success
View Only
View Only
View Only
View Only
View Only
Netskope Cloud Exchange
*The API token generated for the Cloud Exchange role grants access solely based on your specific API setup.
Privilege/Role
API Data Protection
Policies
Reports
End Users
Incident Management
Threat
Tenant Admin
View and Manage
View and Manage
View and Manage
View and Manage
View and Manage
View and Manage
Delegated Admin
View and Manage
View and Manage
View and Manage
View and Manage
View and Manage
View and Manage
Restricted Admin
View Only
View and Manage
View Only
View and Manage
Cloud Intelligence Analyst
View and Manage
View and Manage
Application Risk Analyst
View and Manage
View and Manage
Enterprise Applications Admin
View and Manage
View and Manage
Directory Admin
View Only
View Only
View and Manage
View and Manage
View and Manage
Security Admin
View and Manage
View and Manage
View and Manage
View and Manage
View and Manage
View and Manage
InfoSec Operations Admin
View and Manage
View and Manage
View and Manage
View and Manage
View and Manage
Compliance Office
View Only
View and Manage
View and Manage
View and Manage
Security Analyst
View and Manage
View and Manage
Iaas/PaaS
View and Manage
View and Manage
View and Manage
NS Technical Success
View Only
View Only
View and Manage
View Only
View Only
View Only
Netskope Cloud Exchange
*The API token generated for the Cloud Exchange role grants access solely based on your specific API setup.
Functional Areas and UI Mapping
Each functional area has access to functionality in the UI. The table below shows the general mapping. Note, we do not have a menu item called Advanced Settings but the mapping shows the areas for which we consider to be advanced settings.
Functional Area
UI Component
Administrators
Settings > Administration > Admins
Settings > Administration > Roles
Settings > Administration > Audit Logs
Advanced Settings
Settings > Administration > SSO
Settings > Administration > IP Allowlist
Settings > Tools > Rest API
Settings > Tools > Clear Events
End Users
Settings > Security Cloud Platform > Users
Settings > Security Cloud Platform > Groups
Settings > Security Cloud Platform > Devices
Policies
Everything under Policies (Main Menu)
Settings > Manage
Configure App Access
(previously API-enabled Protection)
Everything under Configure App Access (Main Menu)
Settings > Configure App Access > Classic > SaaS
Settings > Configure App Access > Classic > IaaS
API Data Protection
Policies > API Data Protection
Real-time Protection
Policies > Real-time Protection
Security Posture
Policies > Security Posture
Settings
Everything under Settings
CCI
Everything under Cloud Confidence Index (Main Menu)
Events
Skope IT > Events
SkopeIT> Alerts
Skope IT > Applications
Skope IT > Sites
Skope IT > Users
Advanced Analytics
Everything under Advanced Analytics (Main Menu)
Forensics
Policies > Forensic
Settings > Forensics
Threat
Incident > Anomaly
Incident > Compromised Credentials
Incident > Malware
Incident > Malsites
Create Administrators
Create Roles for Restricted Administrators
Assign Roles to Restricted Administrators
Create a Netskope Support Admin
Multi-Factor Authentication for Netskope Admins
Admin Account Domains
In this Topic
Managing Administrators

---
## Managing Administrators for RBAC V2
**URL:** https://docs.netskope.com/en/managing-administrators-for-rbac-v2/
**Last Modified:** 2025-08-31T01:38:46+00:00
**Scraped:** 2026-08-02T08:37:37.202261+00:00

Managing Administrators for RBAC V2 - Netskope Knowledge Portal
Managing Administrators for RBAC V2
Contact Support to enable this feature set in your account.
Manage Administrators
Create Policy Groups
Create Roles
Admins Settings Page
Create Admins and Assign to Roles
RBAC Best Practices
In this Topic
Managing Administrators for RBAC V2

---
## Tenant Overview
**URL:** https://docs.netskope.com/en/tenant-overview/
**Last Modified:** 2026-07-23T00:25:36+00:00
**Scraped:** 2026-08-02T08:38:18.710815+00:00

Tenant Overview - Netskope Knowledge Portal
Tenant Overview
The widgets on this page provide an overview of the traffic and performance of your tenant. There are two sets of widgets on this page. The top section provides a summary of the last 7 days and cannot be filtered. The Filtered Widgets section provides information based on the timeframe you select using the filters on top of the page. Go to
Digital Experience Management > Tenant Overview
to view this page.
Usage and Session Count
The top section of the page displays information about the data usage, session counts, Netskope POPs in use, Netskope Client versions in use, and number of active users.
Total bytes processed in the last 7 days
: The total number of bytes processed by Netskope in the last 7 days. This widget is RBAC-enabled.
Total uploaded bytes in the last 7 days
: The total number of bytes uploaded by users in the last 7 days. This widget is RBAC-enabled.
Total downloaded bytes in the last 7 days
: The total number of bytes downloaded by users in the last 7 days. This widget is RBAC-enabled.
Daily Session Count for the Last 7 days
: The daily session count for all access methods in the last 7 days. This widget is RBAC-enabled.
POP Usage by Traffic Volume
: The total usage for all access methods distributed by the POP. This widget is RBAC-enabled.
Client Versions In Use
: The total number of sessions with a specific client version in the last 7 days.
Active Users in the Last 7 Days
:  The number of active users in the last 7 days. This widget is RBAC-enabled.
POP & Service Status
: The POP & Service Status map shows you all of the Netskope POPs used by the tenant in the last 90 days, along with the near real-time status of all services in each POP.
Click on a green circle to view the status details of all your services.
The timeframe on these widgets is preset to show data for the last 7 days. Changing the Event Timestamp filter on top of the page does not affect the timeframe on these widgets.
Use the filters on top of the page to view data for a specific timeframe, Netskope POP, Netskope Monitored app, or Access Method under Filtered Widgets. The Access Method filter can only be applied to “Hourly Traffic Volume By POP” and “Unique Active Users Per Hour By POP” widgets.
Filtered Widgets
The widgets provide a view of latency and data usage using graphs. You can use the filters on top of the page to select an event timestamp, Netskope POP, and applications for which you want to view the data.
The
Client to Netskope POP Latency widget
shows you the average round trip time between the end user’s device and the Netskope POP. It does not account for the processing time in the client or in the POP.
Similarly, the
Netskope POP to App Latency
widget shows you the average round trip time observed between the Netskope POP and the destination application. It does not account for the Netskope platform’s processing time.
The
Uploaded & Downloaded Bytes
shows you the average number of bytes that are uploaded and downloaded by the end users. This graph can help you identify peak durations of network traffic. Using this data, you can monitor your network traffic for sudden spikes, or manage your infrastructure maintenance window during off-peak hours. This widget is RBAC-enabled.
The
Hourly Traffic Volume By POP
shows you the total number bytes sent to a POP by the hour on that day. You can use the Access Method filter on top of the page to view data for a specific traffic steering method. This widget is RBAC-enabled.
The
Unique Active Users Per Hour By POP
shows you the number of unique active users connected to a single POP by the hour on that day. You can use the Access Method filter on top of the page to view data for a specific traffic steering method. This widget is RBAC-enabled.
The
Storage Scan Consumption By Month
shows you the volume of data scanned in GB per month for each of the Netskope supported public cloud resources.
In this Topic
Tenant Overview

---
## Configure the Remote Console
**URL:** https://docs.netskope.com/en/configure-the-remote-console/
**Last Modified:** 2025-08-31T01:43:22+00:00
**Scraped:** 2026-08-02T08:39:36.659914+00:00

Configure the Remote Console - Netskope Knowledge Portal
Configure the Remote Console
Configuration of each appliance requires access to the remote console over the IPMI interface.
To configure the remote console:
Make sure the appliance has a network cable attached to its Inbound port. Also, make sure the other end of the network cable is plugged into a switch that allows the appliance to connect to your network.
Plug a cable from your laptop or desktop machine into the IPMI port on the appliance. The IPMI addresses are set to these default values:
IP Address:
192.168.0.2
Subnet Mask:
255.255.255.0
Adjust your laptop or desktop interface’s IP address to be in this subnet (any value of
192.168.0.1
to
192.168.0.254
, except for
192.168.0.2
) and subnet mask of
255.255.255.0
.
Open a browser and enter the IP address
192.168.0.2
in the URL address field. The default login credentials for the IPMI port on the
old appliance with the orange chassis
are
root/netskope
.
The default login credentials for the IPMI port on the
new appliance with the grey chassis
are
ADMIN/netSkope21
.
Enter the credentials in the username and password fields and click
Login
.
After you successfully log in, you should see the System Information page:
Click
Remote Control
in the top menu bar.
Click
Launch Console
. This downloads the file
jviewer.jnlp
to the Download folder. Open the file by double-clicking it.
Important
Make sure you have Java already installed as described in the Prerequisites section.
Caution
Some Java warning messages may show up in a window behind the main screen.
After the console is available, follow the steps described in
Configuring the Management Plane Appliance
and
Configuring the Log Parser Appliance
.
Tip
You may need to click on the console window to direct input to it.
After you have finished setting up the minimal network configuration on an appliance through the IPMI console, you can close your console window. Your appliance should be accessible from the network using ssh at this point.
Remove the network cable from your laptop or desktop machine and restore your laptop or desktop network settings to their previous values.
In this Topic
Configure the Remote Console

---
## Hide Sensitive Data from Admins
**URL:** https://docs.netskope.com/en/hide-sensitive-data-from-admins/
**Last Modified:** 2025-08-31T01:43:15+00:00
**Scraped:** 2026-08-02T08:40:06.877465+00:00

Hide Sensitive Data from Admins - Netskope Knowledge Portal
Hide Sensitive Data from Admins
Admins can be kept from viewing sensitive data, like user names, source IPs, and so on. To do so, create a Role and then apply it to the privileges for an admin.
Go to
Settings > Administration > Roles
.
Click
Create New
. The Create Role dialog box opens.
Enter a role name and description, and then change one of the privileges, like change CCI to View Only. Next, scroll down and select All under Obfuscate.
Click
Save
.
Go to
Administration > Admins
.
Select an admin listed in the Email column. In the Edit Admin dialog box, select the obfuscate role you just created from the Role dropdown list. When finished, click
Update
.
In this Topic
Hide Sensitive Data from Admins

---
## Monitor Status using the Tenant UI
**URL:** https://docs.netskope.com/en/monitor-status-using-the-tenant-ui-144864/
**Last Modified:** 2025-08-31T01:43:01+00:00
**Scraped:** 2026-08-02T08:40:23.577549+00:00

Monitor Status using the Tenant UI - Netskope Knowledge Portal
Monitor Status using the Tenant UI
The logs are processed on the appliance and extracted cloud app events are uploaded to your tenant instance in the Netskope appliance the beginning of each hour. The logs you see in the tenant at the beginning of each hour are for the previous hour, and the latest logs are in the queue.
You can check the status of the log processing on the
Settings > Risk Insights > Log > Upload
page. This page shows the files uploaded, the number of events extracted from the file, and whether a log file is Started, Queued, or Completed. If no events were extracted, refer to the Knowledge Base article
No Events are Extracted
.
You can also monitor the status of the appliance, such as memory,disk space, process status, and so on, from the tenant UI. Go to
Settings > Security Cloud Platform > On-Premises Infrastructure
to see the status. Some of the items displayed under Infrastructure are:
Content: Shows the Success icon
when the latest content software package has been installed.
Serial Number: Shows the serial number of the appliance.
Name: Shows the hostname configured on the appliance.
Configuration: Shows the types of configurations installed on the appliance, like OPLP, Forward Proxy (DPoP), SNMP, and so on.
Status: Shows the Disconnected icon
when the appliance is not operating.
Last Status Change: Shows the last time the appliance refreshed the Status information.
Last Seen: Shows the last time the appliance connected to the backend server. The appliance sends a status update to Netskope backend server every 30 seconds.
Version: Shows the version of software installed.
Click the toggle arrow  to view the details. This view provides additional details of current outstanding events and all the processes running on the appliance, like disk space usage, memory used, etc.
Installed Packages: Shows the Netskope packages installed on the appliance
AD Logs: Shows the AD parser status. When the appliance receives logs from AD Connector, this process is responsible for processing the AD logs files and create the IP to User mapping files.
Log Parser: Shows the status of the log Risk Insights process. The log Risk Insights feature processes the log files and extracts the cloud app events of interest and uploads them to the Netskope tenant.
System: Shows the disk usage, memory usage, CPU load average, and how long the system has been up.
KMIP: Shows the KMIP status when the VA is configured as an On-Premises Key Manager for encryption. This is not applicable for the OPLP.
Syslogng: Shows the status only when the appliance is configured as syslogng.
Log Watcher: Shows the status of the log watcher process, which moves the log files from the
/nslogs/user/upload/<parser>
folder to the
/opt/ns/logcollector/tenant/0/<parser>
folder. Once moved it queues the file for processing.
Create and View Alerts
If the Management Plane is deployed on-premises, then you must setup an SMTP server on the appliance to allow email alerts to be sent from the appliance.
To configure your internal SMTP server on the appliance:
In the tenant UI, go to
Settings > Manage > SMTP Configuration
.
Provide the host name and port of your internal SMTP server.
Choose whether to use SSL and enable certificate validation.
Provide a username and password. Click
Test
.
Setup alerts in the tenant UI.
Go to the
Settings > Security Cloud Platform > On-Premises Infrastructure
page.
Scroll down and click
Configure Alerts
under Infrastructure.
On the Infrastructure Alerts screen, select or add the email recipients you want to alert when status changes.
To access and view alerts in the tenant UI, on the On-Premises Infrastructure page, click
View Logs
. The following information is displayed on the  Infrastructure Logs page.
Time: The date and time at which the alert was created.
Device Serial Number: The serial number of the appliance on which the alert was created.
Device Name: The name of the appliance on which the alert was created.
Severity: The severity of the alert.
Type: The type of alert.
Description: The description of the alert.
In this Topic
Monitor Status using the Tenant UI

---
## Monitor Status using the Tenant UI
**URL:** https://docs.netskope.com/en/monitor-status-using-the-tenant-ui/
**Last Modified:** 2025-09-01T12:48:38+00:00
**Scraped:** 2026-08-02T08:40:25.776560+00:00

Monitor Status using the Tenant UI - Netskope Knowledge Portal
Monitor Status using the Tenant UI
The logs for dedicated log parsing appliances are processed on the appliance and extracted cloud app events are uploaded to your tenant instance in the Netskope appliance the beginning of each hour.
You can check the status of the log processing on the
Settings > Risk Insights > Log > Upload
page. This page shows the files uploaded, the number of events extracted from the file, and whether a log file is Started, Queued, or Completed. If no events were extracted, refer to the Knowledge Base article
No Events are Extracted
.
You can also monitor the status of the appliance, such as memory,process status, and so on, from the tenant UI. Go to
Settings > Security Cloud Platform > On-Premises Infrastructure
to see the status. Some of the items displayed under Infrastructure are:
Content: Shows the Success icon
when the latest content software package has been installed.
Serial Number: Shows the serial number of the appliance.
Name: Shows the hostname configured on the appliance.
Configuration: Shows the types of configurations installed on the appliance, like DNS, Secure Forwarder, Log Parser, and so on.
Status: Shows the Disconnected icon
when the appliance is not operating.
Last Status Change: Shows the last time the appliance refreshed the Status information.
Last Seen: Shows the last time the appliance connected to the backend server. The appliance sends a status update to Netskope backend server every 30 seconds.
Version: Shows the version of software installed.
Click the toggle arrow  to view the details. This view provides additional details of current outstanding events and all the processes running on the appliance, like disk space usage, memory used, etc.
Installed Packages: Shows the Netskope packages installed on the appliance
AD Logs: Shows the AD parser status. When the appliance receives logs from AD Connector, this process is responsible for processing the AD logs files and create the IP to User mapping files.
Log Parser: Shows the status of the log Risk Insights process. The log Risk Insights feature processes the log files and extracts the cloud app events of interest and uploads them to the Netskope tenant.
System: Shows the  memory usage and how long the system has been up.
Syslogng: Shows the status only when the appliance is configured as syslogng.
Log Watcher: Shows the status of the log watcher process, which moves the log files from the
/nslogs/user/upload/<parser>
folder to the
/opt/ns/logcollector/tenant/0/<parser>
folder. Once moved it queues the file for processing.
Create and View Alerts
If the Management Plane is deployed on-premises, then you must setup an SMTP server on the appliance to allow email alerts to be sent from the appliance.
To configure your internal SMTP server on the appliance:
In the tenant UI, go to
Settings > Manage > SMTP Configuration
.
Provide the host name and port of your internal SMTP server.
Choose whether to use SSL and enable certificate validation.
Provide a username and password. Click
Test
.
Setup alerts in the tenant UI.
Go to the
Settings > Security Cloud Platform > On-Premises Infrastructure
page.
Scroll down and click
Configure Alerts
under Infrastructure.
On the Infrastructure Alerts screen, select or add the email recipients you want to alert when status changes.
To access and view alerts in the tenant UI, on the On-Premises Infrastructure page, click
View Logs
. The following information is displayed on the  Infrastructure Logs page.
Time: The date and time at which the alert was created.
Device Serial Number: The serial number of the appliance on which the alert was created.
Device Name: The name of the appliance on which the alert was created.
Severity: The severity of the alert.
Type: The type of alert.
Description: The description of the alert.
In this Topic
Monitor Status using the Tenant UI

---
## Upload Logs to the Netskope Tenant using HTTPS
**URL:** https://docs.netskope.com/en/upload-logs-to-the-netskope-tenant-using-https-144861/
**Last Modified:** 2025-09-01T12:48:59+00:00
**Scraped:** 2026-08-02T08:40:48.231753+00:00

Upload Logs to the Netskope Tenant using HTTPS  - Netskope Knowledge Portal
Upload Logs to the Netskope Tenant using HTTPS
Upload Logs to the Netskope Tenant using HTTPS
Extracted cloud app events from the appliance get uploaded to the Netskope UI using SFTP. This requires connectivity to
upload-
<tenant hostname>
.goskope.com
on port 22. You can also upload logs from the extracted cloud app events by enabling https-upload on port 443.
Note
The domain name shown above applies to release 46 and higher. For deployments on release 45 or lower, use
upload.goskope.com
.
The REST API token needs to be configured on the Netskope UI prior to using the HTTPS log upload. To configure the REST API token, login to the Netskope UI and go to
Settings > Tools > REST API
, and then click
Generate New Token
.
To enable an HTTPS log upload, enter this command at the configuration prompt:
set log-upload https-upload enable
To save the HTTPS configuration, enter
save
at the configuration prompt.
In this Topic
Upload Logs to the Netskope Tenant using HTTPS

---
## Upload Logs to the Netskope Tenant using HTTPS
**URL:** https://docs.netskope.com/en/upload-logs-to-the-netskope-tenant-using-https/
**Last Modified:** 2025-09-01T12:49:00+00:00
**Scraped:** 2026-08-02T08:40:51.536969+00:00

Upload Logs to the Netskope Tenant using HTTPS  - Netskope Knowledge Portal
Upload Logs to the Netskope Tenant using HTTPS
Upload Logs to the Netskope Tenant using HTTPS
Extracted cloud app events from the appliance get uploaded to the Netskope UI using SFTP. This requires connectivity to
upload-
<tenant hostname>
.goskope.com
on port 22. You can also upload logs from the extracted cloud app events by enabling https-upload on port 443.
The REST API token needs to be configured on the Netskope UI prior to using the HTTPS log upload. To configure the REST API token, login to the Netskope UI and go to
Settings > Tools > REST API v1
, and then click
Generate New Token
.
To enable an HTTPS log upload, enter this command at the configuration prompt:
set log-upload https-upload enable
To save the HTTPS configuration, enter
save
at the configuration prompt.
In this Topic
Upload Logs to the Netskope Tenant using HTTPS

---
## Create a Netskope Support Admin
**URL:** https://docs.netskope.com/en/create-a-netskope-support-admin/
**Last Modified:** 2026-07-08T23:48:10+00:00
**Scraped:** 2026-08-02T08:41:03.817340+00:00

Create a Netskope Support Admin - Netskope Knowledge Portal
Create a Netskope Support Admin
You can grant Netskope personnel temporary access to your account through Netskope IdP. This feature is helpful when working with Netskope Support, Professional Services, Customer Experience, etc.
To Grant Access
Navigate to
Settings
>
Administration
>
Administrators & Roles
>
Settings
>
Netskope Personnel
. The Netskope Personnel side panel displays.
Enable the
SSO
Quick Access
radio button. This allows Netskope personnel to log in to your account.
Optionally, enable the
SSO Explicit Access
radio button. This grants Netskope personnel access with an assigned role and an expiration time. To learn more:
Explicit Access for Netskope Personal
Click
Save
.
To Disable Access
Navigate to
Settings
>
Administration
>
Administrators & Roles
>
Settings
>
Netskope Personnel
. The Netskope Personnel side panel displays.
Disable the radio button.
Disabling Explicit Access
: If you toggle off the explicit access feature, you will receive two warning messages indicating that all explicitly added users will be deleted. This action will permanently remove all explicit access accounts. To learn more:
Managing Netskope Personnel Accounts
Click Save. Once access is disabled, any user that tries to log in will see the following error message.
You can view and filter access in the Audit Log.
To View Access
Navigate to
Settings
>
Administration
>
Audit Log
.
The Audit Log shows all users that have admin access to your account. This list includes all internal users and delegated SSO access.
Note
The Last Login column may be blank but that means the delegated admin was last active or logged in prior to this column being added to the UI.
To Filter Access
Navigate to
Settings
>
Administration
>
Audit Log
.
Click
+Add Filter
>
Netskope Personnel
>
Yes
.
The Audit Log page displays with a filtered view showing only the Netskope Personnel users.
RBAC Role Assignment
The following are the permissions provided by Netskope personnel:
Netskope Support – NS technical success
Netskope CX Team – NS technical success
Netskope Professional Services (PS) – NS technical success
Explicit Access for Netskope Personal
Explicit access allows
tenant administrators
to invite and add Netskope personnel to their tenant. This feature provides invited Netskope personnel with enhanced control over the access privileges required to access your environment, offering a more secure and granular approach than the previous Quick Mode (single-click option).
Quick Mode is typically used to invite Netskope Professional Services (PS) and Customer Success (CS) personnel. If no explicit access is defined, a default read-only privilege is applied.
Explicit Access Mode allows you to assign specific roles with limited permissions and set expiration times for these accounts.
If a Netskope support user is added for both Quick Access Mode and Explicit Access Mode, the Explicit Access Mode role privilege will override the Quick Access Mode role privilege.
Prerequisites
The explicit access feature requires RBAC v3 (Role-Based Access Control Version 3) to be enabled in the tenant.
Enabling Explicit Access
After the RBACv3 is enabled by support, go to
Settings
>
Administrators
>
Administrators & Roles
to add Netskope Personnel to your tenant.
Click
Settings
(top right corner of the user listing table) >
Netskope Personal
Toggle the
SSO explicit access
button to
ON
.
Accept the Usage acknowledgment policy and click
Continue
.
Then click
Save
. You can now start inviting Netskope personnel into your tenant.
After saving, the “
Invite Netskope personal
” option is available as a link and an option under the Invite dropdown in the user listing table.
Adding a Netskope Personnel
Navigate to the invite section and click the
Invite Netskope personal
option.
Enter the email address of the Netskope personnel (e.g., xyz@Netskope.com).
You must know the exact email address, as access to the Netskope directory is unavailable.
Select a role for the user. You can choose from custom roles or predefined roles. Roles can be assigned with limited permissions.
Set an expiration time for the account. The default expiration time is 7 days from the creation time. The maximum expiration time is 2 years. There is also an option to set no expiration date.
Once added, the account will be listed as a “
user account only
,” showing details like the role, expiration date, and that it was provisioned by SSO. The icon for Netskope personnel accounts will be distinct.
Managing Netskope Personnel Accounts
User Authentication
: Netskope personnel added via explicit access will log in using Netskope SSO. They will not receive an email invitation for activation, as access is granted directly via SSO.
Extending Expiration Time
: If a Netskope personnel account has expired, you can re-enable it by extending its expiration time.
Disabling Explicit Access
: If you toggle off the explicit access feature, you will receive two warning messages indicating that all explicitly added users will be deleted. This action will permanently remove all explicit access accounts.
Special Scenarios and Important Notes
Handling Existing Local Accounts
: In cases where a local account for a Netskope employee already exists (e.g., from before this feature was available), if you try to invite that same email address via explicit access, a pop-up will ask if you want to delete the local account and create a Netskope personnel account instead. Netskope recommends using SSO for explicit access rather than making local accounts for Netskope personnel. If a Netskope personnel account (via SSO explicit access) already exists, the system will not allow you to create a local account for the same email address.
Note: Netskope Internal Domains. For Netskope.com domain users to be added as administrators, the Netskope.com domain must be configured as an “internal domain” within your tenant.
Limited Access Notification: Netskope personnel who log in with roles that have limited permissions will see a banner indicating “limited access on the dashboard.” For instance, a role might only grant permission to the SSO section under administration.
Access Denial: If a Netskope employee attempts to log in via Netskope SSO, but their email is not explicitly defined under explicit access or quick mode (and the feature is enabled), their access will be denied with an error.
SSO Types for Admins: It’s important to distinguish between SSO Quick Access and SSO Regular Access:
SSO Quick Access (
previously supported
): Based on Identity Provider (IDP) group mapping for predefined roles. Administrators can only delete these roles; no other changes are permitted.
SSO Regular Access (
Regular Admin SSO
): This is the standard SSO configuration for a customer’s own administrators. If an SSO account does not have “Netskope personnel” associated with its email, it is considered the customer’s regular SSO account.
In this Topic
Create a Netskope Support Admin

---
## NewEdge Traffic Management Zones per NPA Tenant
**URL:** https://docs.netskope.com/en/configure-newedge-traffic-management-zones-per-npa-tenant/
**Last Modified:** 2026-03-03T02:38:54+00:00
**Scraped:** 2026-08-02T08:42:29.033649+00:00

NewEdge Traffic Management Zones per NPA Tenant - Netskope Knowledge Portal
NewEdge Traffic Management Zones per NPA Tenant
Netskope Private Access tenants may now take advantage of NewEdge Traffic Management
intent-based
Zones. Some organizations have inline (or
data in motion
) compliance requirements that restrict inline traffic processing to specific geographical regions. You will now be able to restrict traffic to supported Zones.
By default, all tenants are in the Global Zone, which includes all NewEdge DCs. This is generally the best configuration for all tenants, because it provides the best connectivity by allowing access to the largest number and most performant DCs.
Some example Zones are:
United States Zone
European Economic Area (EEA) Zone
Australia Zone
Canada Zone
Many others – Generally any geopolitical region that has more than one NewEdge DC can be selected as a Zone.
In order to support a NewEdge Traffic Management Zones, EDNS/LDNS fallback must be disabled. To disable EDNS/LDNS and in order to have a tenant assigned to a specific Zone, Netskope Support or Customer Success representatives can help.
In this Topic
NewEdge Traffic Management Zones per NPA Tenant

---
## Netskope Tenant Certificate Rotation Guide
**URL:** https://docs.netskope.com/en/netskope-tenant-certificate-rotation-guide/
**Last Modified:** 2026-01-06T21:16:52+00:00
**Scraped:** 2026-08-02T08:44:27.393064+00:00

Netskope Tenant Certificate Rotation Guide - Netskope Knowledge Portal
Netskope Tenant Certificate Rotation Guide
Netskope Tenant CA Rotation Guide 01-06-26
Download
In this Topic
Netskope Tenant Certificate Rotation Guide

---
## Netskope Tenant Plugin
**URL:** https://docs.netskope.com/en/netskope-tenant-plugin/
**Last Modified:** 2026-07-17T00:14:58+00:00
**Scraped:** 2026-08-02T08:46:35.438787+00:00

Netskope Tenant Plugin - Netskope Knowledge Portal
Netskope Tenant Plugin
Release Notes
1.6.1 (Requires minimum Cloud Exchange version 6.1.0)
Added
Added coordinated cleanup of the shared client status iterator so it is removed only when no Netskope plugin (Risk Exchange or Log Shipper) is using it.
Type cast large ID fields to String to avoid UI rounding them off while rendering.
1.6.0
Fixed
Updated the historical pull logic to ensure that valid events within the requested time range from the last batch are processed.
Updated handling for pulling alerts/events from stored checkpoint.
1.5.3
Changed
Improved exception handling when forensics service is not enabled on Netskope Tenant.
Updated tooltip for V1 API token.
Added resolutions for common errors.
1.5.2
Fixed
Updated iterator index with analytics type.
1.5.1
Fixed
Updated WebTx creds retrieval interval on authentication error.
Updated pulling workflow.
1.5.0
Fixed
Added support to pull forensics for DLP Incident events. To pull and ingest these fields update your CLS Netskope plugin version to 2.3.0, CTO Netskope plugin version to 2.3.0 and CE version to 5.1.2.
1.4.2
Fixed
Updated pulling workflow.
Bug Fix.
1.4.1
Fixed
Bug Fix.
1.4.0
Added
Added support for Client status events. To pull and ingest this event type update your CLS Netskope plugin version to 2.2.0.
1.3.0
Added
Enhanced field learning workflow with updated plugin to identify fields and their data types.
1.2.0
Added
Added support for device and content alerts.
1.1.0
Changed
Enhanced pulling workflow.
Updated authentication for V1 token.
1.0.0
Added
Initial release.
This document explains how to configure the Netskope Tenant v1.6.1 plugin in Cloud Exchange. This plugin is responsible for configuring Netskope tenants and collecting alerts, events, and WebTx data from the Netskope tenant.
Starting with Cloud Exchange 5.1.0, Netskope tenants are configured through a Tenant plugin and not through
Settings > Netskope Tenants
.
Prerequisites
To complete this configuration, you need:
Connectivity to a Netskope tenant with permission to generate API tokens.
To pull and ingest Client Status events, you will need to configure the
Log Shipper
plugin.
To pull and ingest Forensics Data for Incident events, you will need Cloud Exchange v5.1.2 or above and CLS Netskope plugin v2.3.0 or above.
Tenant Plugin Support
This plugin is responsible for configuring Netskope tenants and collecting alerts, events, and WebTx data (via Netskope LogStreaming) from the Netskope tenant. To access the plugin, you need a Netskope Tenant.
Data Type
Support
Event Types
Yes (Audit, Application, Infrastructure, Network, Incident, Page, Endpoint, Client status)
Alert Types
Yes (DLP, Malware, Policy, Compromised Credential, Malsite, Quarantine, Remediation, Security Assessment, Watchlist, CTEP, UBA, Device, Content)
WebTx
Yes (via Netskope LogStreaming)
Note
CLS WebTX based on Google Pub Sub Lite is deprecated. Refer to
Netskope Product EOL/EOS Announcements
for more details.
For ingesting WebTX logs to your Log delivery destinations like SIEM, SOAR, XDR, Data Lake, use the
AWS Netskope Log Streaming
or
Azure Netskope Log Streaming
plugin.
Permissions
The required permissions (privilege levels) per plugin are available in the
REST API scopes
.
Need v2 token(RBACv3 API Token) created using the Netskope Cloud Exchange Role.
API Details
Here’s a list of the APIs used.
Validation
API Endpoint
Method
Use Case
/api/v1/app_instances
GET
To validate a v1 token.
/api/v2/events/dataexport/events/alert
GET
To validate a v2 token while configuring tenant.
Alerts
API Endpoint
Method
Use Case
/api/v2/events/dataexport/alerts/dlp
GET
Pull DLP Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/malware
GET
Pull Malware Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/remediation
GET
Pull Remediation Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/securityassessment
GET
Pull Security Assessment Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/ctep
GET
Pull CTEP Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/malsite
GET
Pull Malsite Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/policy
GET
Pull Policy Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/quarantine
GET
Pull Quarantine Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/uba
GET
Pull UBA Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/watchlist
GET
Pull Watchlist Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/device
GET
Pull Device Alerts from the Netskope tenant.
/api/v2/events/dataexport/alerts/content
GET
Pull Content Alerts from the Netskope tenant.
Events
API Endpoint
Method
Use Case
/api/v2/events/dataexport/events/page
GET
Pull Page Events from the Netskope tenant.
/api/v2/events/dataexport/events/application
GET
Pull Application Events from the Netskope tenant.
/api/v2/events/dataexport/events/audit
GET
Pull Audit Events from the Netskope tenant.
/api/v2/events/dataexport/events/infrastructure
GET
Pull Infrastructure Events from the Netskope tenant.
/api/v2/events/dataexport/events/network
GET
Pull Network Events from the Netskope tenant.
/api/v2/events/dataexport/events/incident
GET
Pull Incident Events from the Netskope tenant
/api/v2/incidents/dlpincidents/{id}/forensics
GET
pull Incident Forensics per dlp_incident_id.
/api/v2/events/dataexport/events/endpoint
GET
Pull Endpoint Events from the Netskope tenant.
api/v2/events/dataexport/iterator/netskope_ce_cs_iterator?eventtype=clientstatus
POST
Create a Client Status Iterator.
/api/v2/events/dataexport/iterator/
<iterator_name>
GET
Check Status of a Client Status Iterator.
/api/v2/events/dataexport/iterator/
<iterator_name>
/events?operation=next
GET
Fetch data from a Client Status Iterator.
api/v2/events/dataexport/iterator/
<iterator_name>
DELETE
Delete a Client Status Iterator.
Validate a v1 token
API Endpoint:
https://
<tenant-url>
/api/v1/app_instances
Method:
GET
Request Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Request Parameters
Key
Value
op
list
limit
1
Payload
{"token":
<netskope_api_v1_token>
}
Sample API Response
{
    "status": "success",
    "data": [
        {
            "app": "Oracle Aconex",
            "instance_name": "46",
            "instance_id": "46",
            "type": "Custom",
            "tags": [
                "Unsanctioned"
            ],
            "last_modified": "2025-02-24 09:59:54",
            "custom": "0",
            "app_id": "46"
        }
    ]
}
Validate a v2 Token
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/alert
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "abc350cdb1e1958a03ccd13c",
    "access_method": "Endpoint",
    "acked": "false",
    "action": "block",
    "activity": "Insert",
    "alert": "yes",
    "alert_name": "TestBlock",
    "alert_type": "Device",
    "app": "",
    "category": "",
    "cci": 0,
    "ccl": "unknown",
    "count": 1,
    "device_classification": "not configured",
    "organization_unit": "",
    "os": "macOS",
    "other_categories": [],
    "policy": "TestBlock",
    "timestamp": 1719994603,
    "traffic_type": "",
    "type": "endpoint",
    "ur_normalized": "kmaheshwari@netskope.com",
    "user": "kmaheshwari@netskope.com",
    "userkey": "kmaheshwari@netskope.com",
    "record_type": "alert",
    "to_object": "",
    "account_id": "",
    "CononicalName": "",
    "malsite_country": "",
    "src_geoip_src": 0,
    "object": "",
    "fromlogs": "",
    "ext_labels": [],
    "last_timestamp": 0,
    "justification_type": "",
    "tss_mode": "",
    "user_id": "",
    "password_type": "",
    "suppression_key": "",
    "connection_id": 0,
    "sha256": "",
    "site": "",
    "src_longitude": 0.0,
    "os_version": "",
    "resp_cnt": 0,
    "src_timezone": "",
    "user_confidence_index": 0,
    "browser_version": "",
    "dst_region": "",
    "last_app": "",
    "dlp_rule_count": 0,
    "sessionid": "",
    "profile_id": "",
    "threshold": 0,
    "org": "",
    "suppression_end_time": 0,
    "nsdeviceuid": "",
    "parent_id": "",
    "compliance_standards": [],
    "true_obj_category": "",
    "severity": "",
    "sa_profile_id": 0,
    "malsite_longitude": 0.0,
    "sa_rule_id": "",
    "region_name": "",
    "device": "",
    "dlp_mail_parent_id": "",
    "evt_src_chnl": "",
    "malsite_latitude": 0.0,
    "request_id": 0,
    "sa_rule_severity": "",
    "dst_latitude": 0.0,
    "universal_connector": "",
    "malsite_ip_host": "",
    "referer": "",
    "dst_geoip_src": 0,
    "severity_level": "",
    "conn_starttime": 0,
    "dsthost": "",
    "last_location": "",
    "useragent": "",
    "breach_description": "",
    "shared_domains": "",
    "asset_object_id": "",
    "malicious": "",
    "sa_rule_name": "",
    "breach_target_references": "",
    "justification_reason": "",
    "conn_duration": 0,
    "object_id": "",
    "userPrincipalName": "",
    "alert_id": "",
    "exposure": "",
    "mime_type": "",
    "true_obj_type": "",
    "user_generated": "",
    "total_collaborator_count": 0,
    "browser_session_id": 0,
    "dst_timezone": "",
    "appsuite": "",
    "retro_scan_name": "",
    "page_site": "",
    "last_device": "",
    "dlp_unique_count": 0,
    "sAMAccountName": "",
    "src_zipcode": "",
    "file_size": 0,
    "domain": "",
    "title": "",
    "conn_endtime": 0,
    "dst_location": "",
    "telemetry_app": "",
    "netskope_pop": "",
    "malsite_region": "",
    "serial": "",
    "web_universal_connector": "",
    "modified": 0,
    "iaas_remediated": "",
    "internal_collaborator_count": 0,
    "object_type": "",
    "domain_ip": "",
    "orig_ty": "",
    "threshold_time": 0,
    "src_location": "",
    "dlp_profile": "",
    "data_type": "",
    "web_url": "",
    "src_time": "",
    "severity_level_id": 0,
    "resource_category": "",
    "browser": "",
    "region_id": "",
    "dlp_incident_id": 0,
    "last_country": "",
    "threat_match_value": "",
    "netskope_activity": "",
    "server_bytes": 0,
    "dlp_file": "",
    "two_factor_auth": "",
    "breach_date": 0,
    "url": "",
    "policy_actions": [],
    "req_cnt": 0,
    "external_collaborator_count": 0,
    "dst_country": "",
    "log_file_name": "",
    "scan_type": "",
    "src_region": "",
    "threat_source_id": 0,
    "notify_template": "",
    "malsite_category": [],
    "numbytes": 0,
    "dlp_is_unique_count": "",
    "account_name": "",
    "file_path": "",
    "file_lang": "",
    "suppression_start_time": 0,
    "custom_attr": {},
    "email_source": "",
    "sanctioned_instance": "",
    "owner": "",
    "bypass_traffic": "",
    "src_latitude": 0.0,
    "page": "",
    "dstip": "",
    "hostname": "",
    "dstport": 0,
    "matched_username": "",
    "src_country": "",
    "file_cls_encrypted": false,
    "md5": "",
    "iaas_asset_tags": [],
    "file_type": "",
    "malsite_id": "",
    "app_session_id": 0,
    "protocol": "",
    "userip": "",
    "breach_media_references": "",
    "instance": "",
    "app_activity": "",
    "client_bytes": 0,
    "sa_profile_name": "",
    "instance_id": "",
    "http_transaction_count": 0,
    "breach_id": "",
    "transaction_id": 0,
    "from_user": "",
    "last_region": "",
    "managementID": "",
    "shared_with": "",
    "resource_group": "",
    "appcategory": "",
    "event_type": "",
    "asset_id": "",
    "srcip": "",
    "managed_app": "",
    "dlp_parent_id": 0,
    "breach_score": "",
    "dst_zipcode": "",
    "dlp_rule_severity": "",
    "orignal_file_path": "",
    "threat_match_field": "",
    "dst_longitude": 0.0,
    "external_email": 0,
    "policy_id": "",
    "dlp_rule": ""
}
Get Compromised Credential Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/compromisedcredential
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "20575270a59c8ef1d85d535c",
    "acked": "false",
    "alert": "yes",
    "alert_name": "Secret share",
    "alert_type": "Compromised Credential",
    "app": "Friend2Friend",
    "category": "Cloud Storage",
    "cci": 29,
    "ccl": "poor",
    "count": 1,
    "organization_unit": "netskope.local/Netskope/Active Users/US & International/Full Time",
    "timestamp": 1727659690,
    "type": "nspolicy",
    "ur_normalized": "dte1953ce410-0495t@test.netskope.com",
    "user": "dte1953ce410-0495t@test.netskope.com",
    "userkey": "dte1953ce410-0495t@test.netskope.com",
    "division": "",
    "external_email": 0,
    "mail": "",
    "sAMAccountName": "",
    "password_type": "",
    "userPrincipalName": "",
    "breach_date": 0,
    "sAMAccountType": "",
    "breach_id": "",
    "breach_score": "",
    "department": "",
    "employeeType": "",
    "matched_username": "",
    "breach_media_references": "",
    "email_source": "",
    "breach_description": "",
    "breach_target_references": "",
    "distinguishedName": ""
}
Get DLP Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/dlp
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "31365da11ecc94a0d7edfb6f",
    "access_method": "API Connector",
    "acked": "false",
    "action": "alert",
    "alert": "yes",
    "alert_name": "GDrive Customer metadata shared externally",
    "alert_type": "DLP",
    "app": "Google Drive",
    "appcategory": "Cloud Storage",
    "browser": "unknown",
    "category": "Cloud Storage",
    "ccl": "high",
    "device": "Other",
    "dst_country": "US",
    "dst_geoip_src": 1,
    "dst_latitude": 37.40599060058594,
    "dst_location": "Mountain View",
    "dst_longitude": -122.0785140991211,
    "dst_region": "California",
    "dstip": "172.217.14.78",
    "exposure": "organisation_wide_link",
    "ext_labels": [
        {
            "data_classification_label": "pym/uducbb2126/encryption_level_11",
            "id": "6e05576c-782b-42b4-b8f7-71dfb9ffb5a0",
            "instance": "uducbb2126",
            "name": "encryption_level_11",
            "vendor": "pym"
        },
        {
            "data_classification_label": "ydu/ldmwyo2852/encryption_level_11",
            "id": "20c2b17d-7612-4349-b1e1-62d0d6b48ccb",
            "instance": "ldmwyo2852",
            "name": "encryption_level_11",
            "vendor": "ydu"
        },
        {
            "data_classification_label": "uwa/eqpoco8593/encryption_level_9",
            "id": "6f77b892-3888-4148-8168-d954856d2fea",
            "instance": "eqpoco8593",
            "name": "encryption_level_9",
            "vendor": "uwa"
        }
    ],
    "file_lang": "ENGLISH",
    "file_path": "/My Drive/Clickhouse/Tenant Migration across MPs",
    "file_size": 196869,
    "file_type": "application/vnd.google-apps.document",
    "instance": "netskope.com",
    "instance_id": "netskope.com",
    "local_sha256": "edd7df8bb5a774a7531a389287a3bd71cf8e62197d93a205860003ed8339a4de",
    "md5": "4bf7680195ecaed55e3edabb5d95ca01",
    "mime_type": "application/vnd.google-apps.document",
    "modified": 1613760236,
    "object": "Tenant Migration across MPs",
    "object_id": "14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "object_type": "File",
    "organization_unit": "netskope.local/Netskope/Active Users/US & International/Full Time",
    "os": "unknown",
    "owner": "foobar",
    "policy": "GDrive Customer metadata shared externally",
    "request_id": "2459149802892628500",
    "scan_type": "Ongoing",
    "site": "Google Drive",
    "suppression_key": "Tenant Migration across MPs",
    "timestamp": 1716551379,
    "title": "Tenant Migration across MPs",
    "traffic_type": "CloudApp",
    "type": "nspolicy",
    "ur_normalized": "rowkuxqaxdxnlnlw",
    "url": "https://drive.google.com/open?id=14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "user": "RoWkuxQAxDxNlNLw",
    "userkey": "RoWkuxQAxDxNlNLw",
    "record_type": "alert",
    "page_site": "",
    "act_user": "",
    "src_longitude": 0.0,
    "dst_timezone": "",
    "device_classification": "",
    "to_user": "",
    "dlp_file": "",
    "connection_id": 0,
    "external_collaborator_count": 0,
    "incident_id": 0,
    "dlp_fingerprint_classification": "",
    "activity": "",
    "from_storage": "",
    "user_confidence_index": 0,
    "browser_version": "",
    "dynamic_classification": "",
    "smtp_to": [],
    "dlp_rule_severity": "",
    "shared_with": "",
    "outer_doc_type": 0,
    "orignal_file_path": "",
    "channel": "",
    "data_type": "",
    "userip": "",
    "sanctioned_instance": "",
    "src_region": "",
    "true_filetype": "",
    "dlp_rule_count": 0,
    "shared_domains": "",
    "owner_pdl": "",
    "dlp_unique_count": 0,
    "transaction_id": 0,
    "browser_session_id": 0,
    "userCountry": "",
    "bcc": "",
    "displayName": "",
    "srcip": "",
    "dlp_mail_parent_id": "",
    "hostname": "",
    "classification_name": "",
    "protocol": "",
    "sAMAccountName": "",
    "violating_user": "",
    "manager": "",
    "src_time": "",
    "src_country": "",
    "true_obj_category": "",
    "message_size": 0,
    "dlp_fingerprint_score": 0,
    "src_geoip_src": 0,
    "os_version": "",
    "true_type_id": 0,
    "to_storage": "",
    "tss_mode": "",
    "managed_app": "",
    "file_password_protected": "",
    "dlp_incident_id": 0,
    "managementID": "",
    "dlp_fingerprint_match": "",
    "src_timezone": "",
    "mail": "",
    "total_collaborator_count": 0,
    "from_user": "",
    "app_activity": "",
    "user_id": "",
    "custom_attr": {},
    "group": "",
    "file_cls_encrypted": false,
    "universal_connector": "",
    "message_id": "",
    "file_category": "",
    "dlp_parent_id": 0,
    "sub_type": "",
    "src_latitude": 0.0,
    "userPrincipalName": "",
    "dlp_is_unique_count": "",
    "dlp_rule_score": 0,
    "src_zipcode": "",
    "dlp_rule": "",
    "referer": "",
    "app_session_id": 0,
    "parent_id": "",
    "retro_scan_name": "",
    "src_location": "",
    "dst_zipcode": "",
    "dlp_profile": "",
    "true_obj_type": "",
    "violating_user_type": "",
    "policy_id": "",
    "web_universal_connector": "",
    "appsuite": "",
    "severity": "",
    "sha256": "",
    "collaborated": "",
    "page": ""
}
Get Malware Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/malware
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "TSS-scan": "TSS-Scan-V3",
    "_id": "389551cd1bdaa1ae4947c334",
    "access_method": "Client",
    "acked": "false",
    "action": "Detection",
    "activity": "Browse",
    "alert": "yes",
    "alert_name": "GT:JS.Adware.Popunder.4.34B7F109",
    "alert_type": "Malware",
    "app": "hitomi",
    "app_name": "hitomi",
    "app_session_id": 4113602168491103340,
    "appcategory": "Adult Content - Pornography",
    "browser_session_id": 2610528494199657827,
    "category": "Adult Content - Pornography",
    "cci": "",
    "ccl": "",
    "connection_id": 5767115909713174088,
    "count": 1,
    "detection_engine": "Netskope AV",
    "device": "Linux Device",
    "device_classification": "not configured",
    "dst_country": "UA",
    "dst_latitude": 50.45465850830078,
    "dst_location": "Kyiv",
    "dst_longitude": 30.523799896240234,
    "dst_region": "Kyiv",
    "dst_timezone": "Europe/Kyiv",
    "dst_zipcode": "N/A",
    "dstip": "185.255.122.62",
    "file_category": "Text",
    "file_id": "1dda26cbf77944ccb931f3444b554c74",
    "file_size": 2277,
    "file_type": "text/html",
    "hostname": "ub20-50-5-28",
    "incident_id": 7718454634228557343,
    "instance": "",
    "local_md5": "cda70ab0130f915723a53a5d9270e7a5",
    "malware_id": "3d81bec28fff68180bf8baa5727924ba",
    "malware_name": "GT:JS.Adware.Popunder.4.34B7F109",
    "malware_profile": "1",
    "malware_severity": "high",
    "malware_type": "Virus",
    "managed_app": "no",
    "md5": "cda70ab0130f915723a53a5d9270e7a5",
    "ml_detection": "None",
    "object_type": "File",
    "organization_unit": "",
    "os": "Linux",
    "os_version": "Linux 20.04",
    "page": "hitomi.la/",
    "page_site": "Web Background",
    "policy": "Threat-Malware-Policy-Crest-SRE-Test",
    "policy_id": "342F7551F4D4469E47D7736209486319 2024-07-01 16:28:12.174470",
    "protocol": "HTTPS/1.1",
    "request_id": 2907585389470724608,
    "scanner_result": "malicious",
    "severity": "High",
    "severity_id": 3,
    "sha256": "d330ea88b7a0c2f9190717d8f39a2e3942474c3fefe8b68112e7b93fde0fa9d4",
    "site": "hitomi",
    "src_country": "IN",
    "src_latitude": 23.0276,
    "src_location": "Ahmedabad",
    "src_longitude": 72.5871,
    "src_region": "Gujarat",
    "src_time": "Wed Aug 14 13:48:00 2024",
    "src_timezone": "Asia/Kolkata",
    "src_zipcode": "382350",
    "srcip": "110.226.17.67",
    "timestamp": 1723623535,
    "traffic_type": "Web",
    "transaction_id": 7718454634228557343,
    "true_filetype": "HTML",
    "tss_mode": "inline",
    "type": "nspolicy",
    "ur_normalized": "nipun.brahmbhatt@crestdata.ai",
    "url": "hitomi.la/",
    "user": "nipun.brahmbhatt@crestdata.ai",
    "user_id": "nipun.brahmbhatt@crestdata.ai",
    "userip": "10.50.5.28",
    "record_type": "alert",
    "department": "",
    "scan_time": 0,
    "tss_scan_failed": "",
    "usr_udf_supervisorname": "",
    "instance_id": "",
    "nsdeviceuid": "",
    "modified_date": 0,
    "dst_geoip_src": 0,
    "local_sha256": "",
    "sha1": "",
    "usr_udf_primarydomain": "",
    "fastscan_results": "",
    "sanctioned_instance": "",
    "company": "",
    "user_confidence_index": 0,
    "src_geoip_src": 0,
    "usr_udf_businesssegmentlevel1": "",
    "referer": "",
    "parent_id": "",
    "created_date": 0,
    "usr_udf_businesssegmentlevel2": "",
    "filename": "",
    "from_user": "",
    "file_path": "",
    "manager": "",
    "browser": "",
    "detection_type": "",
    "title": "",
    "object_id": "",
    "mime_type": "",
    "usr_display_name": "",
    "usr_udf_businesssegmentlevel4": "",
    "userPrincipalName": "",
    "appsuite": "",
    "scan_type": "",
    "tss_license": "",
    "managementID": "",
    "usr_status": "",
    "object": "",
    "custom_attr": {},
    "userCountry": "",
    "usr_title": "",
    "usr_udf_businesssegmentlevel3": "",
    "file_name": "",
    "shared_type": "",
    "usr_udf_companyname": "",
    "shared_with": "",
    "tss_fail_reason": "",
    "usr_udf_supervisorid": "",
    "browser_version": "",
    "usr_udf_employeeid": ""
}
Get Remediation Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/remediation
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "448ca50ee6142a954d64c577",
    "access_method": "API Connector",
    "acked": "true",
    "action": "alert",
    "activity": "Download",
    "alert": "yes",
    "alert_name": "Remediation alert",
    "alert_type": "Remediation",
    "app": "Clanwilliam Health",
    "appcategory": "Cloud Storage",
    "browser": "unknown",
    "category": "Cloud Storage",
    "cci": 9,
    "ccl": "poor",
    "count": 1,
    "device": "Other",
    "dst_country": "NL",
    "dst_geoip_src": 2,
    "dst_latitude": 52.3759,
    "dst_location": "Amsterdam",
    "dst_longitude": 4.8975,
    "dst_region": "North Holland",
    "dst_zipcode": "1012",
    "dstip": "31.186.239.8",
    "file_size": 118585,
    "file_type": "application/vnd.google-apps.document",
    "instance_id": "netskope.com",
    "md5": "4bf7680195ecaed55e3edabb5d95ca01",
    "object": "VTRapjqhGbaDXqHR",
    "object_type": "File",
    "organization_unit": "netskope.local/Netskope/Active Users/US & International/Full Time",
    "os": "Windows 7.0",
    "policy": "policy_ga34",
    "request_id": "2459149802892628500",
    "site": "Clanwilliam Health",
    "src_country": "NL",
    "src_geoip_src": 2,
    "src_latitude": 52.3759,
    "src_location": "Amsterdam",
    "src_longitude": 4.8975,
    "src_region": "North Holland",
    "src_zipcode": "1012",
    "srcip": "31.186.239.8",
    "timestamp": 1727659690,
    "traffic_type": "CloudApp",
    "type": "nspolicy",
    "ur_normalized": "dte1953ce410-0268t@test.netskope.com",
    "url": "https://drive.google.com/open?id=14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "user": "dte1953ce410-0268t@test.netskope.com",
    "managementID": "",
    "from_user": "",
    "os_version": "",
    "app_session_id": 0,
    "malware_severity": "",
    "actions_taken": "",
    "transaction_id": 0,
    "notify_template": "",
    "page": "",
    "browser_session_id": 0,
    "src_time": "",
    "tss_mode": "",
    "managed_app": "",
    "severity": "",
    "nsdeviceuid": "",
    "remediation_profile": "",
    "dlp_profile": "",
    "malware_name": "",
    "endpoints": "",
    "connection_id": 0,
    "policy_id": "",
    "endpoint_count": 0,
    "dst_timezone": "",
    "profile_hits": [],
    "malware_id": "",
    "hostname": "",
    "edr_app": "",
    "device_classification": "",
    "userip": "",
    "appsuite": "",
    "protocol": "",
    "incident_id": 0,
    "src_timezone": "",
    "sanctioned_instance": "",
    "page_site": "",
    "malware_type": "",
    "all_policy_matches": []
}
Get Security Assessment Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/securityassessment
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "15bbca35f014e9618efdc629",
    "_insertion_epoch_timestamp": 1727659690,
    "access_method": "API Connector",
    "acked": "false",
    "action": "alert",
    "activity": "Introspection Scan",
    "alert": "yes",
    "alert_name": "security-accessment-alert",
    "alert_type": "Security Assessment",
    "app": "LinkedIn",
    "appcategory": "Cloud Storage",
    "browser": "unknown",
    "category": "Cloud Storage",
    "ccl": "medium",
    "count": 1,
    "device": "Other",
    "dst_country": "FR",
    "dst_geoip_src": 1,
    "dst_latitude": 48.883411,
    "dst_location": "Puteaux",
    "dst_longitude": 2.23894,
    "dst_region": "Ile-de-France",
    "dstip": "193.248.155.211",
    "exposure": "organisation_wide_link",
    "file_lang": "ENGLISH",
    "file_path": "\\/My Drive\\/Clickhouse\\/Tenant Migration across MPs",
    "file_size": 196869,
    "file_type": "application\\/vnd.google-apps.document",
    "instance": "netskope.com",
    "instance_id": "netskope.com",
    "md5": "4bf7680195ecaed55e3edabb5d95ca01",
    "mime_type": "application\\/vnd.google-apps.document",
    "modified": 1613760236,
    "object": "OlWmGNTVpEVLCgWo",
    "object_id": "14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "object_type": "File",
    "organization_unit": "netskope.local\\/Netskope\\/Active Users\\/US & International\\/Full Time",
    "os": "unknown",
    "other_categories": [],
    "owner": "foobar",
    "policy": "GDrive Customer metadata shared externally",
    "request_id": "2459149802892628500",
    "sa_profile_id": 1,
    "sa_profile_name": "CRzpqYgDBoKRThmb",
    "sa_rule_id": "icveiWoIMGqmEfUy",
    "sa_rule_name": "RLYnpTzcFeiRcQYr",
    "sa_rule_severity": "High",
    "scan_type": "Ongoing",
    "shared_with": "none",
    "site": "LinkedIn",
    "src_country": "FR",
    "src_geoip_src": 1,
    "src_latitude": 48.883411,
    "src_location": "Puteaux",
    "src_longitude": 2.23894,
    "src_region": "Ile-de-France",
    "srcip": "193.248.155.211",
    "suppression_key": "Tenant Migration across MPs",
    "timestamp": 1727659690,
    "traffic_type": "CloudApp",
    "type": "nspolicy",
    "ur_normalized": "crest_sup_de_202112031049-0@crest.netskope.com",
    "url": "https:\\/\\/drive.google.com\\/open?id=14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "user": "crest_sup_de_202112031049-0@crest.netskope.com",
    "usergroup": [],
    "userkey": "crest_sup_de_202112031049-0@crest.netskope.com"
}
Get CTEP Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/ctep
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_correlation_id": "d54406dc-5457-4699-8754-c8eece88a804",
    "_event_id": "8de38a44-4ae5-44ac-a097-f9e3ce2aac2a",
    "_forwarded_by": "na",
    "_generator_id": "ad4c77a8-ac83-4493-936c-8d6394038556",
    "_id": "d62273697847e13a884e7562",
    "_insertion_epoch_timestamp": 1727659690,
    "_raw_event_inserted_at": 1676185709059,
    "_seq_id": 117219,
    "_service_identifier": "na",
    "_skip_geoip_lookup": "yes",
    "access_method": "API Connector",
    "acked": "false",
    "action": "block",
    "activity": "Login Successful",
    "alert": "yes",
    "alert_name": "c2",
    "alert_type": "c2",
    "app": "X3host",
    "appcategory": "Cloud Storage",
    "browser": "unknown",
    "category": "Cloud Storage",
    "cci": 16,
    "ccl": "poor",
    "count": 1,
    "device": "11-inch iPad Pro",
    "dst_country": "US",
    "dst_geoip_src": 2,
    "dst_latitude": 45.8234,
    "dst_location": "Boardman",
    "dst_longitude": -119.7257,
    "dst_region": "Oregon",
    "dst_zipcode": "97818",
    "dstip": "52.218.153.131",
    "exposure": "organisation_wide_link",
    "file_lang": "ENGLISH",
    "file_path": "/My Drive/Clickhouse/Tenant Migration across MPs",
    "file_size": 118783,
    "file_type": "application/vnd.google-apps.document",
    "instance": "netskope.com",
    "instance_id": "netskope.com",
    "legal_hold_profile_name": "oejTJocnOabNirPx",
    "lh_custodian_email": "ELGkdoczLAkrQMuq",
    "lh_custodian_name": "iRwQlRYvjwsFlVpg",
    "lh_dest_app": "dOkImPvoHqwfXFaU",
    "lh_dest_instance": "LKMHXgSCmGTmVbZL",
    "lh_fileid": "taAjyAQRSWraghfP",
    "lh_filename": "rsjjtAjqpCcYjaOU",
    "lh_filepath": "IhYDbjTXhzqtUZeD",
    "lh_original_filename": "vWijvCFegHYDULbn",
    "lh_shared": "WCLXYCUEBjqOlWHt",
    "lh_shared_with": "SwUYQdzFHslSQoxr",
    "lh_version": 1,
    "local_sha256": "fd856057ed7703e9b53458c7dbb6a3dc4ce9b957f3b307d81f06bf09c9bd8de3",
    "md5": "4bf7680195ecaed55e3edabb5d95ca01",
    "mime_type": "application/vnd.google-apps.document",
    "modified": 1613760236,
    "object": "OLizsiNCpTCziLEC",
    "object_id": "14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "object_type": "File",
    "organization_unit": "netskope.local/Netskope/Active Users/US & International/Full Time",
    "os": "iOS  9.6",
    "other_categories": [],
    "owner": "dte1953ce410-0778t@test.netskope.com",
    "policy": "policy_ga13",
    "request_id": "2459149802892628500",
    "scan_type": "Ongoing",
    "site": "X3host technologies",
    "src_country": "NL",
    "src_geoip_src": 2,
    "src_latitude": 52.3759,
    "src_location": "Amsterdam",
    "src_longitude": 4.8975,
    "src_region": "North Holland",
    "src_zipcode": "1012",
    "srcip": "31.186.239.204",
    "suppression_key": "Tenant Migration across MPs",
    "timestamp": 1727659690,
    "traffic_type": "CloudApp",
    "type": "nspolicy",
    "ur_normalized": "dte1953ce410-0494t@test.netskope.com",
    "url": "https://drive.google.com/open?id=14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "user": "dte1953ce410-0494t@test.netskope.com",
    "userkey": "dte1953ce410-0494t@test.netskope.com"
}
Get Malsite Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/malsite
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "01f6ca78bec577883076a738",
    "access_method": "Client",
    "acked": "false",
    "action": "block",
    "alert": "yes",
    "alert_name": "bget.ru",
    "alert_type": "malsite",
    "app": "",
    "app_session_id": 4910069257574835437,
    "appcategory": "Security Risk - Compromised/malicious sites",
    "browser_session_id": 1141245448937753175,
    "category": "Security Risk - Compromised/malicious sites",
    "cci": 0,
    "ccl": "unknown",
    "connection_id": 0,
    "count": 1,
    "device": "Linux Device",
    "device_classification": "not configured",
    "dst_country": "RU",
    "dst_latitude": 59.9417,
    "dst_location": "St Petersburg",
    "dst_longitude": 30.3096,
    "dst_region": "St.-Petersburg",
    "dst_timezone": "Europe/Moscow",
    "dst_zipcode": "195213",
    "dstip": "5.101.158.143",
    "dstport": 443,
    "hostname": "ip-172-31-37-148",
    "incident_id": 7989528656047608655,
    "ja3": "07ff1e545ef8ab3fcf8a4dc9272221c2",
    "ja3s": "NotAvailable",
    "malicious": "yes",
    "malsite_category": [
        "Malicious Site"
    ],
    "malsite_country": "RU",
    "malsite_id": "ae7c3ade12353ae7165e9b2f",
    "malsite_ip_host": "5.101.158.143",
    "malsite_latitude": 59.9417,
    "malsite_longitude": 30.3096,
    "malsite_region": "St.-Petersburg",
    "managed_app": "no",
    "notify_template": "block_page.html",
    "organization_unit": "",
    "os": "Linux",
    "os_version": "Linux 22.04",
    "other_categories": [
        "Security Risk",
        "Security Risk - Compromised/malicious sites"
    ],
    "page": "bget.ru/",
    "page_site": "bget",
    "policy": "TestMalsite2",
    "policy_id": "F1AE7109B6FC54098C582D3B0F149521 2024-05-28 13:48:56.784091",
    "protocol": "HTTPS/1.1",
    "request_id": 2851228580036571136,
    "severity_level": "med",
    "severity_level_id": 1,
    "site": "bget",
    "src_country": "US",
    "src_latitude": 39.0469,
    "src_location": "Ashburn",
    "src_longitude": -77.4903,
    "src_region": "Virginia",
    "src_time": "Tue May 28 10:07:00 2024",
    "src_timezone": "America/New_York",
    "src_zipcode": "20149",
    "srcip": "18.209.94.135",
    "telemetry_app": "",
    "threat_match_field": "domain",
    "threat_match_value": "bget.ru",
    "threat_source_id": 1,
    "timestamp": 1716905279,
    "traffic_type": "Web",
    "transaction_id": 7989528656047608655,
    "type": "malsite",
    "ur_normalized": "keshavhazard@gmail.com",
    "url": "bget.ru/",
    "user": "keshavhazard@gmail.com",
    "useragent": "python-requests/2.25.1",
    "userip": "172.31.37.148",
    "record_type": "alert",
    "malsite_reputation": "",
    "object": "",
    "org": "",
    "fromlogs": "",
    "log_file_name": "",
    "req_cnt": 0,
    "browser_version": "",
    "numbytes": 0,
    "department": "",
    "division": "",
    "retro_scan_name": "",
    "sfwder": "",
    "browser": "",
    "custom_attr": {},
    "malsite_confidence": 0,
    "server_bytes": 0,
    "client_bytes": 0,
    "malsite_first_seen": 0,
    "co": "",
    "sAMAccountName": "",
    "src_geoip_src": 0,
    "gateway": "",
    "referer": "",
    "suppression_start_time": 0,
    "resp_cnt": 0,
    "conn_duration": 0,
    "serial": "",
    "malsite_hostility": "",
    "dsthost": "",
    "dst_geoip_src": 0,
    "universal_connector": "",
    "malsite_active": "",
    "from_user": "",
    "object_type": "",
    "suppression_end_time": 0,
    "malsite_last_seen": 0,
    "severity": "",
    "aggregated_user": "",
    "malsite_consecutive": "",
    "appsuite": ""
}
Get Policy Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/policy
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "3ceffe626afca6f5d46befb6",
    "access_method": "Client",
    "acked": "false",
    "action": "block",
    "alert": "yes",
    "alert_name": "testprivateapp with2nd opt",
    "alert_type": "policy",
    "app": "[ExtraHop-Demo]",
    "appcategory": "n/a",
    "category": "n/a",
    "cci": 0,
    "ccl": "unknown",
    "client_bytes": 0,
    "client_packets": 0,
    "count": 1,
    "device": "Windows",
    "dsthost": "netskope.atlassian.net",
    "dstip": "",
    "dstport": 443,
    "end_time": "2025-02-28T08:22:47+00:00",
    "hostname": "WIN11-50-12-151",
    "ip_protocol": "TCP",
    "network_session_id": "9452921695540616650",
    "num_sessions": 1,
    "numbytes": 0,
    "organization_unit": "",
    "os": "Windows",
    "os_version": "11.0.22621",
    "other_categories": [],
    "policy": "testprivateapp with2nd opt",
    "protocol": "Http",
    "protocol_port": "TCP:443",
    "publisher_cn": "",
    "publisher_name": "",
    "server_bytes": 0,
    "server_packets": 0,
    "session_duration": 0,
    "site": "netskope.atlassian.net",
    "srcip": "",
    "srcport": 30700,
    "start_time": "2025-02-28T08:22:32+00:00",
    "timestamp": 1740731072,
    "total_packets": 0,
    "traffic_type": "PrivateApp",
    "tunnel_id": "53125",
    "tunnel_type": "NPA",
    "tunnel_up_time": 0,
    "type": "network",
    "ur_normalized": "tanushree.kurup@crestdata.ai",
    "user": "tanushree.kurup@crestdata.ai",
    "userip": "",
    "record_type": "alert",
    "suppression_key": "",
    "app_activity": "",
    "file_type": "",
    "url": "",
    "policy_id": "",
    "custom_connector": "",
    "quarantine_profile": "",
    "q_original_shared": "",
    "file_path": "",
    "profile_emails": [],
    "referer": "",
    "md5": "",
    "redirect_url": "",
    "page_site": "",
    "malware_name": "",
    "suppression_end_time": 0,
    "user_id": "",
    "distinguishedName": "",
    "severity": "",
    "src_timezone": "",
    "tss_mode": "",
    "managed_app": "",
    "tss_fail_reason": "",
    "src_geoip_src": 0,
    "owner": "",
    "aggregated_user": "",
    "group": "",
    "total_collaborator_count": 0,
    "userCountry": "",
    "browser": "",
    "to_user": "",
    "from_object": "",
    "ext_labels": [],
    "shared_with": "",
    "useragent": "",
    "sessionid": "",
    "network": "",
    "malicious": "",
    "quarantine_file_id": "",
    "appsuite": "",
    "remediation_profile": "",
    "universal_connector": "",
    "mime_type": "",
    "browser_version": "",
    "src_zipcode": "",
    "access_key_id": "",
    "src_latitude": 0.0,
    "malware_type": "",
    "dynamic_classification": "",
    "src_region": "",
    "q_original_version": "",
    "instance_id": "",
    "message_id": "",
    "sfwder": "",
    "q_admin": "",
    "q_app": "",
    "object_type": "",
    "log_file_name": "",
    "malware_severity": "",
    "retro_scan_name": "",
    "displayName": "",
    "justification_reason": "",
    "q_instance": "",
    "src_location": "",
    "gateway": "",
    "forward_to_proxy_xau": "",
    "justification_type": "",
    "smtp_to": [],
    "app_session_id": 0,
    "request_id": 0,
    "app_scopes": "",
    "parent_id": "",
    "file_category": "",
    "file_id": "",
    "dlp_profile": "",
    "nsdeviceuid": "",
    "risk_level": "",
    "encrypt_failure": "",
    "quarantine_file_name": "",
    "src_longitude": 0.0,
    "file_size": 0,
    "org": "",
    "user_tmp": "",
    "activity_status": "",
    "threat_match_value": "",
    "malsite_category": [],
    "dst_timezone": "",
    "all_policy_matches": [],
    "incident_id": 0,
    "orignal_file_path": "",
    "object_id": "",
    "act_user": "",
    "http_status": "",
    "dst_country": "",
    "from_user": "",
    "req_cnt": 0,
    "transaction_id": 0,
    "browser_session_id": 0,
    "sanctioned_instance": "",
    "from_storage": "",
    "tss-mode": "",
    "cc": "",
    "activity": "",
    "sAMAccountName": "",
    "scan_type": "",
    "serial": "",
    "src_time": "",
    "managementID": "",
    "object": "",
    "q_original_filepath": "",
    "custom_attr": {},
    "shared_domains": "",
    "q_original_filename": "",
    "notify_template": "",
    "connection_id": 0,
    "telemetry_app": "",
    "threat_source_id": 0,
    "user_confidence_index": 0,
    "TSS-scan": "",
    "internal_collaborator_count": 0,
    "last_name": "",
    "mail": "",
    "sAMAccountType": "",
    "memberOf": "",
    "smtp_status": "",
    "Title": "",
    "dst_location": "",
    "bcc": "",
    "dst_geoip_src": 0,
    "exposure": "",
    "activity_type": "",
    "dlp_fail_reason": "",
    "dst_zipcode": "",
    "message_size": 0,
    "suppression_start_time": 0,
    "trust_computer_checked": "",
    "device_classification": "",
    "instance": "",
    "to_storage": "",
    "dst_latitude": 0.0,
    "division": "",
    "object_count": 0,
    "to_object": "",
    "modified": 0,
    "sender": "",
    "dst_region": "",
    "page": "",
    "conn_duration": 0,
    "two_factor_auth": "",
    "dst_longitude": 0.0,
    "data_type": "",
    "quarantine_profile_id": "",
    "malware_id": "",
    "manager": "",
    "src_country": "",
    "event_type": "",
    "external_collaborator_count": 0,
    "resp_cnt": 0,
    "threat_match_field": "",
    "tss_scan_failed": "",
    "dlp_scan_failed": "",
    "sha256": ""
}
Get Quarantine Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/quarantine
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "63d6a681f0d64a6f41cc084c",
    "_insertion_epoch_timestamp": 1727659690,
    "access_method": "API Connector",
    "acked": "false",
    "action": "quarantine-sahil",
    "activity": "Login Successful",
    "alert": "yes",
    "alert_name": "quarantine-alert",
    "alert_type": "quarantine",
    "app": "Dropbox",
    "appcategory": "Cloud Storage",
    "browser": "unknown",
    "category": "Cloud Storage",
    "cci": 81,
    "ccl": "high",
    "count": 1,
    "device": "Other",
    "dst_country": "US",
    "dst_geoip_src": 2,
    "dst_latitude": 33.1432,
    "dst_location": "San Marcos",
    "dst_longitude": -117.1666,
    "dst_region": "California",
    "dst_zipcode": "92069",
    "dstip": "98.176.143.16",
    "exposure": "organisation_wide_link",
    "file_lang": "ENGLISH",
    "file_path": "\\/My Drive\\/Clickhouse\\/Tenant Migration across MPs",
    "file_size": 196869,
    "file_type": "application\\/vnd.google-apps.document",
    "instance": "netskope.com",
    "instance_id": "netskope.com",
    "md5": "4bf7680195ecaed55e3edabb5d95ca01",
    "mime_type": "application\\/vnd.google-apps.document",
    "modified": 1613760236,
    "object": "weclTNVzKoULFCYX",
    "object_id": "14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "object_type": "File",
    "organization_unit": "netskope.local\\/Netskope\\/Active Users\\/US & International\\/Full Time",
    "os": "unknown",
    "other_categories": [],
    "owner": "foobar",
    "policy": "GDrive Customer metadata shared externally",
    "q_admin": "KgBNclCNvMfSfwAe",
    "q_app": "Box",
    "q_instance": "IXlwfxAfRQMyUbso",
    "q_original_filename": "huSgEkeGhFjPDLhS",
    "q_original_filepath": "oJmMLhuvhIyXlarC",
    "q_original_shared": "private",
    "q_original_version": "1",
    "q_shared_with": "PqtCjqtPLVOOFkWk",
    "quarantine_action_reason": "TuJbfomareEgmNNT",
    "quarantine_app": "Amazon S3",
    "quarantine_failure": "mDsCCrKldEQdhrEF",
    "quarantine_file_id": "jeCCFYBKuaBggvol",
    "quarantine_file_name": "GEXNzZEGpZFQAuUv",
    "quarantine_profile": "fQECcfyXhgGUOJSO",
    "quarantine_profile_id": "xfFlQTBQWxjnIsXZ",
    "request_id": "2459149802892628500",
    "scan_type": "Ongoing",
    "shared_with": "none",
    "site": "Dropbox",
    "src_country": "DE",
    "src_geoip_src": 2,
    "src_latitude": 50.1188,
    "src_location": "Frankfurt am Main",
    "src_longitude": 8.6843,
    "src_region": "Hesse",
    "src_zipcode": "60313",
    "srcip": "8.39.144.84",
    "suppression_key": "Tenant Migration across MPs",
    "timestamp": 1727659690,
    "traffic_type": "CloudApp",
    "type": "nspolicy",
    "ur_normalized": "crest_sup_de_202112031049-0@crest.netskope.com",
    "url": "https:\\/\\/drive.google.com\\/open?id=14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "user": "crest_sup_de_202112031049-0@crest.netskope.com",
    "usergroup": [],
    "userkey": "crest_sup_de_202112031049-0@crest.netskope.com"
}
Get UBA Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/uba
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "b7dce8f570123bdd868a8315",
    "access_method": "UCI Impact API",
    "acked": "false",
    "action": "anomaly_detection",
    "activity": "ActivityForUciImpactAPI",
    "alert": "yes",
    "alert_id": "505464b05529c82e34d31970",
    "alert_name": "External alert from Netskope due to Risky User",
    "alert_type": "uba",
    "anomaly_type": "Fact",
    "app": "",
    "appcategory": "n/a",
    "category": "n/a",
    "cci": 0,
    "ccl": "unknown",
    "count": 1,
    "createdTime": "2025-02-24 08:15:55.461000",
    "device": "Other",
    "event_type": "uba_analytics",
    "instance_id": "",
    "organization_unit": "",
    "policy": "External alert received via REST API",
    "score": 1,
    "severity": "informational",
    "src_country": "IN",
    "src_geoip_src": 2,
    "src_latitude": 23.0276,
    "src_location": "Ahmedabad",
    "src_longitude": 72.5871,
    "src_region": "Gujarat",
    "src_zipcode": "380009",
    "srcip": "122.170.162.148",
    "timestamp": 1740384954,
    "type": "nspolicy",
    "ur_normalized": "tanushree.kurup@crestdata.ai",
    "user": "tanushree.kurup@crestdata.ai",
    "userkey": "tanushree.kurup@crestdata.ai",
    "windowId": 1740355200000,
    "record_type": "alert",
    "last_device": "",
    "surhn": "",
    "policy_id": "",
    "uba_ap1": "",
    "evt_src_chnl": "",
    "all_policy_matches": [],
    "threshold": 0,
    "web_universal_connector": "",
    "user_category": "",
    "managementID": "",
    "division": "",
    "download_app": "",
    "user_id": "",
    "dst_longitude": 0.0,
    "audit_type": "",
    "object_count": 0,
    "policy_name": "",
    "activity_status": "",
    "group": "",
    "act_user": "",
    "referer": "",
    "connection_id": 0,
    "app_category": "",
    "bin_timestamp": 0,
    "hostname": "",
    "app_activity": "",
    "md5": "",
    "risk_level_id": 0,
    "suppression_end_time": 0,
    "protocol": "",
    "request_type": "",
    "request_id": 0,
    "app_session_id": 0,
    "User_SPACE_Id": "",
    "user_name": "",
    "last_timestamp": 0,
    "netskope_activity": "",
    "dst_geoip_src": 0,
    "tss_scan_failed": "",
    "loginurl": "",
    "threshold_time": 0,
    "risk_level": "",
    "managed_app": "",
    "browser_version": "",
    "file_category": "",
    "from_user_category": "",
    "page": "",
    "last_location": "",
    "url": "",
    "uba_ap2": "",
    "sanctioned_instance": "",
    "object_id": "",
    "dst_timezone": "",
    "custom_attr": {},
    "to_object": "",
    "dst_country": "",
    "traffic_type": "",
    "telemetry_app": "",
    "page_site": "",
    "file_size": 0,
    "scopes": [],
    "anomalyData": {},
    "os": "",
    "audit_category": "",
    "tss_fail_reason": "",
    "userip": "",
    "last_app": "",
    "incident_id": 0,
    "suppression_start_time": 0,
    "dst_zipcode": "",
    "dstip": "",
    "policy_actions": [],
    "browser": "",
    "src_time": "",
    "sAMAccountName": "",
    "two_factor_auth": "",
    "uba_inst2": "",
    "site": "",
    "displayName": "",
    "sha256": "",
    "object": "",
    "last_country": "",
    "to_user": "",
    "object_type": "",
    "manager": "",
    "last_region": "",
    "dst_region": "",
    "dst_latitude": 0.0,
    "shared_credential_user": "",
    "file_type": "",
    "tss_mode": "",
    "appsuite": "",
    "device_classification": "",
    "logintype": "",
    "AccountType": "",
    "os_version": "",
    "parent_id": "",
    "TSS-scan": "",
    "user_role": "",
    "dst_location": "",
    "to_user_category": "",
    "user_confidence_index": 0,
    "mail": "",
    "browser_session_id": 0,
    "src_timezone": "",
    "useragent": "",
    "employeeType": "",
    "from_user": "",
    "uba_inst1": "",
    "User_SPACE_Name": "",
    "userPrincipalName": "",
    "transaction_id": 0,
    "distinguishedName": "",
    "profile_id": ""
}
Get Watchlist Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/watchlist
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "ad921f96aaf7dc5b6fe5d628",
    "access_method": "API Connector",
    "acked": "true",
    "activity": "Upload",
    "alert": "yes",
    "alert_name": "watchlist fired",
    "alert_type": "watchlist",
    "app": "Amazon App Suite",
    "appcategory": "Cloud Storage",
    "browser": "unknown",
    "category": "Cloud Storage",
    "cci": 89,
    "ccl": "high",
    "count": 1,
    "device": "Other",
    "dst_country": "IN",
    "dst_geoip_src": 2,
    "dst_latitude": 19.0748,
    "dst_location": "Mumbai",
    "dst_longitude": 72.8856,
    "dst_region": "Maharashtra",
    "dst_zipcode": "400072",
    "dstip": "182.75.130.70",
    "exposure": "organisation_wide_link",
    "file_lang": "ENGLISH",
    "file_path": "/My Drive/Clickhouse/Tenant Migration across MPs",
    "file_size": 119268,
    "file_type": "application/vnd.google-apps.document",
    "instance": "netskope.com",
    "instance_id": "netskope.com",
    "local_sha256": "aa477dd147d603cd0bd65b6dfb09021654e212aa3200ceb03e3a1e1d0fb37fdb",
    "md5": "4bf7680195ecaed55e3edabb5d95ca01",
    "mime_type": "application/vnd.google-apps.document",
    "modified": 1613760236,
    "object": "uVwtiXcnOjCdpJHt",
    "object_id": "14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "object_type": "File",
    "organization_unit": "netskope.local/Netskope/Active Users/US & International/Full Time",
    "os": "Windows 8.0",
    "owner": "dte1953ce410-0545t@test.netskope.com",
    "policy": "policy_ga26",
    "request_id": "2459149802892628500",
    "scan_type": "Ongoing",
    "site": "Amazon App Suite",
    "src_country": "DE",
    "src_geoip_src": 2,
    "src_latitude": 50.1188,
    "src_location": "Frankfurt am Main",
    "src_longitude": 8.6843,
    "src_region": "Hesse",
    "src_zipcode": "60313",
    "srcip": "8.39.144.84",
    "suppression_key": "Tenant Migration across MPs",
    "timestamp": 1727659690,
    "traffic_type": "CloudApp",
    "type": "nspolicy",
    "ur_normalized": "dte1953ce410-0191t@test.netskope.com",
    "url": "https://drive.google.com/open?id=14WLYNjJxKgEyqIoNAcb57aPGx9_klcxTo3MyjF82rGg",
    "user": "dte1953ce410-0191t@test.netskope.com",
    "userkey": "dte1953ce410-0191t@test.netskope.com",
    "dst_timezone": "",
    "two_factor_auth": "",
    "dlp_fail_reason": "",
    "title": "",
    "conn_duration": 0,
    "shared_domains": "",
    "user_id": "",
    "notify_template": "",
    "severity_id": 0,
    "TSS-scan": "",
    "universal_connector": "",
    "to_user_category": "",
    "web_url": "",
    "severity": "",
    "netskope_activity": "",
    "malware_severity": "",
    "dlp_is_unique_count": "",
    "sAMAccountName": "",
    "hostname": "",
    "sanctioned_instance": "",
    "object_count": 0,
    "dlp_rule": "",
    "protocol": "",
    "file_id": "",
    "audit_type": "",
    "internal_collaborator_count": 0,
    "dlp_scan_failed": "",
    "appsuite": "",
    "dlp_rule_severity": "",
    "telemetry_app": "",
    "to_user": "",
    "true_obj_category": "",
    "useragent": "",
    "shared_with": "",
    "justification_reason": "",
    "dlp_parent_id": 0,
    "referer": "",
    "src_timezone": "",
    "connection_id": 0,
    "app_session_id": 0,
    "from_user_category": "",
    "client_bytes": 0,
    "malware_name": "",
    "total_collaborator_count": 0,
    "policy_id": "",
    "workspace": "",
    "data_type": "",
    "dlp_profile": "",
    "act_user": "",
    "malware_profile": "",
    "file_name": "",
    "fromlogs": "",
    "ml_detection": "",
    "app_activity": "",
    "malware_id": "",
    "dstport": 0,
    "transaction_id": 0,
    "detection_engine": "",
    "to_storage": "",
    "parent_id": "",
    "managed_app": "",
    "external_collaborator_count": 0,
    "nsdeviceuid": "",
    "tss_fail_reason": "",
    "managementID": "",
    "workspace_id": "",
    "true_obj_type": "",
    "justification_type": "",
    "aggregated_user": "",
    "network": "",
    "org": "",
    "page_site": "",
    "userPrincipalName": "",
    "tss_mode": "",
    "suppression_end_time": 0,
    "true_type_id": 0,
    "server_bytes": 0,
    "manager": "",
    "suppression_start_time": 0,
    "file_category": "",
    "app_name": "",
    "audit_category": "",
    "incident_id": 0,
    "serial": "",
    "resp_cnt": 0,
    "browser_version": "",
    "all_policy_matches": [],
    "enterprise": "",
    "numbytes": 0,
    "device_classification": "",
    "from_object": "",
    "dlp_rule_count": 0,
    "dsthost": "",
    "src_time": "",
    "user_category": "",
    "browser_session_id": 0,
    "sfwder": "",
    "scanner_result": "",
    "dlp_file": "",
    "os_version": "",
    "to_object": "",
    "malware_type": "",
    "log_file_name": "",
    "web_universal_connector": "",
    "enterprise_id": "",
    "dlp_incident_id": 0,
    "from_user": "",
    "userip": "",
    "page": "",
    "req_cnt": 0,
    "from_storage": "",
    "tss_scan_failed": "",
    "local_md5": ""
}
Get Device Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/device
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "983681ec8804b23e77c2c292",
    "access_method": "Endpoint",
    "action": "block",
    "activity": "Insert",
    "alert": "yes",
    "alert_name": "TestBlock",
    "alert_type": "Device",
    "computer_name": "N49J4M9T3C",
    "count": 1,
    "device_classification": "not configured",
    "organization_unit": "",
    "os": "macOS",
    "os_details": "Mac OS X Sonoma 14.3.1 arm64",
    "policy": "TestBlock",
    "policy_action": "block",
    "policy_name_enforced": "TestBlock",
    "timestamp": 1720005433,
    "traffic_type": "",
    "type": "endpoint",
    "ur_normalized": "kmaheshwari@netskope.com",
    "usb_device_id": "USB\\VID_03f0&PID_1985&REV_0110",
    "usb_device_name": "USB Flash Drive",
    "usb_device_sn": "070D2C206FCFA597",
    "usb_device_type": "usb mass storage",
    "usb_product_id": "6533",
    "usb_vendor_id": "HP",
    "user": "kmaheshwari@netskope.com",
    "userkey": "kmaheshwari@netskope.com",
    "record_type": "alert",
    "connection_type": "",
    "driver": "",
    "os_user_name": "",
    "usb_is_encrypted": false,
    "location": "",
    "custom_attr": {}
}
Get Content Alerts
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/alerts/content
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "3f14cdb17c8385f9a6acfab4",
    "access_method": "Endpoint",
    "action": "block",
    "activity": "Create",
    "alert": "yes",
    "alert_name": "mmm1",
    "alert_type": "Content",
    "app": "DesktopServicesHelper",
    "computer_name": "N49J4M9T3C",
    "count": 1,
    "destination_file_directory": "/Volumes/KALI LINUX",
    "destination_file_name": "urls.txt",
    "destination_file_path": "/Volumes/KALI LINUX/urls.txt",
    "device_classification": "not configured",
    "dlp_incident_id": 8329186087212438192,
    "dlp_profile": "DLPTest",
    "file_size": 52483,
    "file_type": "Plain Text file",
    "incident_id": 8329186087212438192,
    "md5": "da3faaff0b406f6aa4685aee47ece41c",
    "organization_unit": "",
    "os": "macOS",
    "os_details": "Mac OS X Sonoma 14.3.1 arm64",
    "os_user_name": "kmaheshwari",
    "pid": "0",
    "policy": "mmm1",
    "policy_action": "block",
    "policy_name_enforced": "mmm1",
    "process_name": "DesktopServicesHelper",
    "process_path": "/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/Resources",
    "sha256": "23a129d56da1579a68862808a22b7b3e1d64682cc7d4c725fdc8a8c7980310b6",
    "site": "DesktopServicesHelper",
    "timestamp": 1719993896,
    "traffic_type": "",
    "type": "endpoint",
    "ur_normalized": "kmaheshwari@netskope.com",
    "usb_device_type": "usb mass storage",
    "user": "kmaheshwari@netskope.com",
    "userkey": "kmaheshwari@netskope.com",
    "record_type": "alert",
    "custom_attr": {},
    "process_cert_subject": "",
    "device": ""
}
Page Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/page
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "56758f371f4e65c4049d423e",
    "access_method": "Client",
    "app": "Microsoft Accounts",
    "appcategory": "Application Suite",
    "bypass_reason": "SSL Do Not Decrypt Bypass Policy Matched",
    "bypass_traffic": "yes",
    "category": "Application Suite",
    "cci": 84,
    "ccl": "high",
    "connection_id": 0,
    "count": 1,
    "domain": "ecs.office.com",
    "dst_country": "US",
    "dst_latitude": 47.6722,
    "dst_location": "Redmond",
    "dst_longitude": -122.1257,
    "dst_region": "Washington",
    "dst_timezone": "America/Los_Angeles",
    "dst_zipcode": "98073",
    "dstip": "52.123.128.14",
    "dstport": 443,
    "netskope_pop": "IN-BOM2",
    "organization_unit": "",
    "os_version": "Windows NT 11.0",
    "other_categories": [
        "Technology",
        "Application Suite"
    ],
    "page": "ecs.office.com",
    "policy": "Default Microsoft appsuite SSL do not decrypt rule",
    "request_id": 3051109095898995457,
    "site": "Microsoft Office 365 Suite",
    "src_country": "IN",
    "src_latitude": 21.7003,
    "src_location": "Bharūch",
    "src_longitude": 72.9782,
    "src_region": "Gujarat",
    "src_time": "Fri Feb 28 14:26:08 2025",
    "src_timezone": "Asia/Kolkata",
    "src_zipcode": "392012",
    "srcip": "103.108.207.58",
    "ssl_decrypt_policy": "yes",
    "timestamp": 1740732961,
    "traffic_type": "CloudApp",
    "transaction_id": 0,
    "type": "connection",
    "ur_normalized": "tanushree.kurup@crestdata.ai",
    "url": "ecs.office.com",
    "user": "tanushree.kurup@crestdata.ai",
    "user_generated": "yes",
    "userip": "10.50.12.151",
    "userkey": "tanushree.kurup@crestdata.ai",
    "record_type": "page",
    "useragent": "",
    "CononicalName": "",
    "forward_to_proxy_profile": "",
    "http_transaction_count": 0,
    "resp_content_type": "",
    "org": "",
    "browser_version": "",
    "conn_starttime": 0,
    "os": "",
    "network": "",
    "device": "",
    "req_cnt": 0,
    "src_geoip_src": 0,
    "conn_endtime": 0,
    "dst_geoip_src": 0,
    "hostname": "",
    "client_bytes": 0,
    "dsthost": "",
    "userPrincipalName": "",
    "numbytes": 0,
    "fromlogs": "",
    "rbi_template_name": "",
    "resp_cnt": 0,
    "browser_session_id": 0,
    "resp_content_len": 0,
    "server_bytes": 0,
    "forward_to_proxy_xau": "",
    "conn_duration": 0,
    "serial": "",
    "sAMAccountName": "",
    "log_file_name": "",
    "rbi_template_id": "",
    "dynamic_classification": "",
    "browser": "",
    "severity": "",
    "suppression_end_time": 0,
    "custom_attr": {},
    "action": "",
    "suppression_start_time": 0,
    "sessionid": "",
    "protocol": "",
    "app_session_id": 0
}
Get Application Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/application
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "5af424a2871523b6e13f853f",
    "access_method": "Client",
    "activity": "Download",
    "alert": "no",
    "app": "ContentSquare",
    "app_session_id": 8320876311700568950,
    "appcategory": "Web Analytics",
    "browser": "Edge",
    "browser_session_id": 5471226135867547944,
    "browser_version": "133.0.0.0",
    "category": "Web Analytics",
    "cci": 60,
    "ccl": "medium",
    "connection_id": 0,
    "count": 1,
    "device": "Windows Device",
    "device_classification": "not configured",
    "dst_country": "IE",
    "dst_latitude": 53.3382,
    "dst_location": "Dublin",
    "dst_longitude": -6.2591,
    "dst_region": "Leinster",
    "dst_timezone": "Europe/Dublin",
    "dst_zipcode": "D02",
    "dstip": "52.48.68.180",
    "dstport": 443,
    "hostname": "WIN11-50-12-151",
    "ja3": "261219d3f4c7b45e9e6014a0084dc181",
    "ja3s": "f4febc55ea12b31ae17cfb7e614afda8",
    "managed_app": "no",
    "netskope_pop": "IN-BOM2",
    "object": "pageview",
    "object_type": "File",
    "organization_unit": "",
    "os": "Windows 11",
    "os_version": "Windows NT 11.0",
    "other_categories": [
        "Content Server",
        "Web Analytics"
    ],
    "page": "c.contentsquare.net/pageview",
    "page_site": "contentsquare",
    "policy_id": "8467252215149297331 2025-02-19 10:04:24.766887",
    "protocol": "HTTPS/1.1",
    "request_id": 3045298505167235584,
    "severity": "unknown",
    "site": "ContentSquare",
    "src_country": "IN",
    "src_latitude": 23.0276,
    "src_location": "Ahmedabad",
    "src_longitude": 72.5871,
    "src_region": "Gujarat",
    "src_time": "Thu Feb 20 14:00:08 2025",
    "src_timezone": "Asia/Kolkata",
    "src_zipcode": "380006",
    "srcip": "182.69.215.65",
    "telemetry_app": "",
    "timestamp": 1740040217,
    "traffic_type": "CloudApp",
    "transaction_id": 1737423402988911503,
    "type": "nspolicy",
    "universal_connector": "yes",
    "ur_normalized": "tanushree.kurup@crestdata.ai",
    "url": "c.contentsquare.net/pageview",
    "user": "tanushree.kurup@crestdata.ai",
    "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "userip": "10.50.12.151",
    "userkey": "tanushree.kurup@crestdata.ai",
    "record_type": "application",
    "suppression_key": "",
    "app_activity": "",
    "file_type": "",
    "dlp_incident_id": 0,
    "custom_connector": "",
    "file_path": "",
    "referer": "",
    "md5": "",
    "suppression_end_time": 0,
    "user_id": "",
    "tss_mode": "",
    "channel_id": "",
    "dlp_rule_count": 0,
    "web_universal_connector": "",
    "tss_fail_reason": "",
    "src_geoip_src": 0,
    "owner": "",
    "alert_type": "",
    "total_collaborator_count": 0,
    "to_user": "",
    "ext_labels": [],
    "shared_with": "",
    "sessionid": "",
    "client_bytes": 0,
    "appsuite": "",
    "mime_type": "",
    "dlp_rule_severity": "",
    "workspace_id": "",
    "instance_id": "",
    "logintype": "",
    "policy": "",
    "log_file_name": "",
    "retro_scan_name": "",
    "justification_reason": "",
    "user_category": "",
    "netskope_activity": "",
    "justification_type": "",
    "smtp_to": [],
    "parent_id": "",
    "nsdeviceuid": "",
    "dlp_profile": "",
    "file_lang": "",
    "file_size": 0,
    "userPrincipalName": "",
    "org": "",
    "audit_type": "",
    "title": "",
    "orignal_file_path": "",
    "object_id": "",
    "dsthost": "",
    "from_user": "",
    "req_cnt": 0,
    "sanctioned_instance": "",
    "dlp_rule": "",
    "loginurl": "",
    "scan_type": "",
    "sAMAccountName": "",
    "serial": "",
    "managementID": "",
    "custom_attr": {},
    "from_user_category": "",
    "notify_template": "",
    "dlp_parent_id": 0,
    "user_confidence_index": 0,
    "internal_collaborator_count": 0,
    "dlp_unique_count": 0,
    "dlp_mail_parent_id": "",
    "true_obj_category": "",
    "dst_geoip_src": 0,
    "exposure": "",
    "dlp_is_unique_count": "",
    "numbytes": 0,
    "dlp_fail_reason": "",
    "suppression_start_time": 0,
    "audit_category": "",
    "true_obj_type": "",
    "data_center": "",
    "instance": "",
    "server_bytes": 0,
    "modified": 0,
    "action": "",
    "conn_duration": 0,
    "data_type": "",
    "fromlogs": "",
    "resp_cnt": 0,
    "workspace": "",
    "dlp_file": "",
    "CononicalName": "",
    "tss_scan_failed": "",
    "dlp_scan_failed": "",
    "sha256": ""
}
Get Audit Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/audit
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "audit_log_event": "Rest API V2 Call",
    "severity_level": 2,
    "supporting_data": {
        "data_type": "policy",
        "data_values": [
            "200",
            "POST",
            "/api/v2/policy/urllist/deploy",
            "trid=22f0b0dfb2b8d75d27aa528ff6040e5d.1740723551"
        ]
    },
    "timestamp": 1740723551,
    "type": "admin_audit_logs",
    "user": "DO-NOT-DELETE",
    "organization_unit": "",
    "ur_normalized": "do-not-delete",
    "count": 1,
    "_id": "074fdfdb6974f8960bfaede9",
    "record_type": "audit",
    "sAMAccountName": "",
    "details": [],
    "ccl": "",
    "userPrincipalName": ""
}
Get Infrastructure Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/infrastructure
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "timestamp": 1727659690,
    "severity": "high",
    "alarm_name": "No_events_from_device",
    "device_name": "panw-dpop-1",
    "metric_value": 43831789,
    "alarm_description": "Events from 仕事 device not received in the last 24 hours",
    "serial": "FF00A7BFFA4E6165E",
    "_insertion_epoch_timestamp": 1727659690,
    "supporting_data": "",
    "_id": "613ee55ec9d868fc47654a73"
}
Get Network Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/network
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "f67629951b42c8e556062456",
    "access_method": "Client",
    "action": "block",
    "app": "Domain Name Service (DNS)",
    "appcategory": "Shopping",
    "category": "Shopping",
    "cci": 0,
    "ccl": "unknown",
    "client_bytes": 0,
    "client_packets": 0,
    "count": 1,
    "device": "Other",
    "domain": "",
    "dst_geoip_src": 2,
    "dsthost": "",
    "dstip": "10.50.1.16",
    "dstport": 5353,
    "end_time": "2025-02-28T09:34:08+00:00",
    "flow_status": "close",
    "ip_protocol": "UDP",
    "numbytes": 0,
    "organization_unit": "",
    "os": "Windows NT 11.0",
    "policy": "default",
    "publisher_name": "",
    "server_bytes": 0,
    "server_packets": 0,
    "session_duration": 0,
    "site": "dns",
    "src_country": "IN",
    "src_geoip_src": 2,
    "src_latitude": 21.7003,
    "src_location": "Bharūch",
    "src_longitude": 72.9782,
    "src_region": "Gujarat",
    "src_zipcode": "392011",
    "srcip": "103.108.207.58",
    "srcport": 5353,
    "start_time": "2025-02-28T09:34:08+00:00",
    "timestamp": 1740735248,
    "total_packets": 0,
    "traffic_type": "non-web",
    "tunnel_id": "1138033360427841",
    "type": "network",
    "ur_normalized": "tanushree.kurup@crestdata.ai",
    "user": "tanushree.kurup@crestdata.ai",
    "userip": "10.50.12.151",
    "userkey": "tanushree.kurup@crestdata.ai",
    "record_type": "network",
    "qdomain": "",
    "dst_region": "",
    "userPrincipalName": "",
    "dst_country": "",
    "tunnel_type": "",
    "dst_zipcode": "",
    "num_sessions": 0,
    "domain_ip": "",
    "dst_longitude": 0.0,
    "protocol": "",
    "tunnel_up_time": 0,
    "protocol_port": "",
    "network_session_id": "",
    "os_version": "",
    "dst_latitude": 0.0,
    "sAMAccountName": "",
    "hostname": "",
    "custom_attr": {},
    "publisher_cn": "",
    "dst_location": ""
}
Get Incident Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/incident
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "6d462e0db470c7247e75322fd380031271d1be18db9d707ef6f3affc792f11b1",
    "access_method": "Endpoint Protection",
    "acting_user": "kmaheshwari@netskope.com",
    "activity": "Create",
    "app": "DesktopServicesHelper",
    "assignee": "None",
    "dlp_incident_id": 7268524954762607217,
    "dlp_match_info": [
        {
            "dlp_action": "block",
            "dlp_forensic_id": 1711868037568704387,
            "dlp_policy": "mmm1",
            "dlp_profile_name": "DLPTest",
            "dlp_rules": []
        }
    ],
    "file_path": "/Volumes/KALI LINUX/urls.txt",
    "file_size": 52483,
    "file_type": "Plain Text file",
    "md5": "da3faaff0b406f6aa4685aee47ece41c",
    "object": "urls.txt",
    "object_id": "hash_kmaheshwari@netskope.com_da3faaff0b406f6aa4685aee47ece41c_7b4a2e1f194ccb4e8eca958a472bfe3c3741d7a6",
    "severity": "Low",
    "status": "new",
    "timestamp": 1719993903,
    "title": "urls.txt",
    "user": "kmaheshwari@netskope.com",
    "record_type": "incident",
    "instance": "",
    "src_location": "",
    "app_session_id": 0,
    "zip_file_id": "",
    "connection_id": 0,
    "destination_site": "",
    "to_user": "",
    "latest_incident_id": 0,
    "from_user": "",
    "site": "",
    "dst_location": "",
    "inline_dlp_match_info": [],
    "destination_instance_id": "",
    "instance_id": "",
    "channel": "",
    "original_file_snapshot_id": "",
    "bcc": "",
    "referer": "",
    "dlp_file": "",
    "destination_app": "",
    "true_obj_type": "",
    "file_lang": "",
    "url": "",
    "true_obj_category": "",
    "cc": "",
    "owner_pdl": "",
    "classification": "",
    "object_type": "",
    "ext_labels": [],
    "exposure": "",
    "dlp_parent_id": 0,
    "owner": "",
    "user_id": ""
}
Get Incident Forensics
API Endpoint:
https://
<tenant-url>
/api/v2/incidents/dlpincidents/{id}/forensics
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Request Parameters
Key
Value
dlp_incident_id in path param
dlp_incident_id
Sample API Response
{
"status": "success",
"data": {
"meta": "{\"metadata_content\":\"filename: sensitive_data_onedrive_share.txt file_md5: 0bcafac7ce40ad3ebad1664307a046f1 file_type: text/plain file_lang: ENGLISH object_id: {\\\"drive_id\\\": \\\"b!PM0toX-2uEqSwuqUx0SzyDAe0n7GMw1Eok5wsoIE5ALI55tDhn-rSJB-vB4UWs5e\\\", \\\"driveitem_id\\\": \\\"014GLSS7Z2KV57XD3LXNFLWFO3HXHVREJB\\\", \\\"site_collection_id\\\": \\\"a12dcd3c-b67f-4ab8-92c2-ea94c744b3c8\\\"} ns_text_classifier: others \",\"dlp_match_info\":[{\"dlp_profile_name\":\"DLP-PCI\",\"dlp_rules\":[{\"dlp_rule_name\":\"Bank-CC\",\"dlp_rule_severity\":\"Low\",\"dlp_incident_rule_count\":3,\"dlp_data_identifiers\":[[{\"start_offset\":41,\"score\":1,\"end_offset\":56,\"entity_name\":\"industries/banking/bank_names/us\",\"type\":\"content\",\"prefix\":\"Number\\n\\n\\n\\n\",\"match\":\"American Express\",\"suffix\":\"\\n\\n\"},{\"start_offset\":59,\"score\":1,\"end_offset\":73,\"entity_name\":\"numbers/payment_card_numbers/major\",\"type\":\"content\",\"match\":\"378282XXXXX0005\",\"suffix\":\"\\n\\n\\n\\nAmerican\"}],[{\"start_offset\":78,\"score\":1,\"end_offset\":93,\"entity_name\":\"industries/banking/bank_names/us\",\"type\":\"content\",\"prefix\":\"378282XXXXX0005\\n\\n\\n\\n\",\"match\":\"American Express\",\"suffix\":\"\\n\\n\"},{\"start_offset\":96,\"score\":1,\"end_offset\":110,\"entity_name\":\"numbers/payment_card_numbers/major\",\"type\":\"content\",\"match\":\"371449XXXXX8431\",\"suffix\":\"\\n\\n\\n\\nAmerican\"}],[{\"start_offset\":115,\"score\":1,\"end_offset\":130,\"entity_name\":\"industries/banking/bank_names/us\",\"type\":\"content\",\"prefix\":\"371449XXXXX8431\\n\\n\\n\\n\",\"match\":\"American Express\",\"suffix\":\" Corporate\"},{\"start_offset\":143,\"score\":1,\"end_offset\":157,\"entity_name\":\"numbers/payment_card_numbers/major\",\"type\":\"content\",\"prefix\":\"\\n\\n\",\"match\":\"378734XXXXX1000\",\"suffix\":\"\\n\\n\\n\\nAustralian\"}]]}],\"dlp_action\":\"quarantine\",\"action_threshold_met\":true,\"dlp_policy\":\"CDS Data Protection Policy\",\"dlp_scan_type\":\"Ongoing\",\"dlp_policy_hash\":\"policy hash\"},{\"dlp_profile_name\":\"US Financial Data\",\"dlp_rules\":[{\"dlp_rule_name\":\"US-Bank-CC\",\"dlp_rule_severity\":\"Low\",\"dlp_incident_rule_count\":2,\"dlp_data_identifiers\":[[{\"start_offset\":19,\"score\":1,\"end_offset\":29,\"entity_name\":\"numbers/payment_card_number_terms/eng\",\"type\":\"content\",\"prefix\":\"Type\\n\\n\",\"match\":\"Credit Card\",\"suffix\":\" Number\"},{\"start_offset\":41,\"score\":1,\"end_offset\":56,\"entity_name\":\"industries/banking/bank_names/us\",\"type\":\"content\",\"prefix\":\"\\n\\n\\n\\n\",\"match\":\"American Express\",\"suffix\":\"\\n\\n\"},{\"start_offset\":59,\"score\":1,\"end_offset\":73,\"entity_name\":\"numbers/payment_card_numbers/major\",\"type\":\"content\",\"match\":\"378282XXXXX0005\",\"suffix\":\"\\n\\n\\n\\nAmerican\"}],[{\"start_offset\":115,\"score\":1,\"end_offset\":130,\"entity_name\":\"industries/banking/bank_names/us\",\"type\":\"content\",\"prefix\":\"3714XXXXXXXX31\\n\\n\\n\\n\",\"match\":\"American Express\",\"suffix\":\" Corporate\"},{\"start_offset\":143,\"score\":1,\"end_offset\":157,\"entity_name\":\"numbers/payment_card_numbers/major\",\"type\":\"content\",\"prefix\":\"\\n\\n\",\"match\":\"378734XXXXX1000\",\"suffix\":\"\\n\\n\\n\\nAustralian\"},{\"start_offset\":203,\"score\":1,\"end_offset\":213,\"entity_name\":\"numbers/payment_card_number_terms/eng\",\"type\":\"content\",\"prefix\":\"...5610591081018250\\n\\n\\n\\n\",\"match\":\"Diners Club\",\"suffix\":\"\\n\\n30569309025904\"}]]}],\"dlp_action\":\"quarantine\",\"action_threshold_met\":true,\"dlp_policy\":\"CDS Data Protection Policy\",\"dlp_scan_type\":\"Ongoing\",\"dlp_policy_hash\":\"policy hash\"}]}",
"content": " Credit Card Type\n\nCredit Card Number\n\n\n\nAmerican Express\n\n37XXXXXXXXX0005\n\n\n\nAmerican Express\n\n37XXXXXXXXX8431\n\n\n\nAmerican Express Corporate\n\n37XXXXXXXXX1000\n\n\n\nAustralian BankCard\n\n5610XXXXXXXX50\n\n\n\nDiners Club\n\n30569XXXXXXXX5904\n\n\n\nDiners Club\n\n3852XXXXXXXX37\n\n\n\nDiscover\n\n60111XXXXXXXX117\n\n\n\nDiscover\n\n6011XXXXXXXX424\n\n\n\nJCB\n\n35301XXXXXXXX00\n\n\n\nJCB\n\n356XXXXXXXX05\n\n\n\nMasterCard\n\n555XXXXXXXX444\n\n\n\nMasterCard\n\n5105XXXXXXXX00\n\n\n\nVisa\n\n41XXXXXXXX111\n\n\n\nVisa\n\n401XXXXXXXX1881\n\n\n\nVisa\n\n422XXXXXXXX222"
}
}
Get Endpoint Events
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/events/endpoint
Method:
GET
Request Headers
Key
Value
Netskope-API-Token
<netskope_api_v2_token>
User-Agent
netskope-ce-6.1.0
Sample API Response
{
    "_id": "dffd23ac520f696e1c4bd020",
    "access_method": "Endpoint",
    "activity_type": "Process Start",
    "alert": "no",
    "alert_generated": false,
    "computer_name": "win11-50-1-92",
    "device_type": "Bluetooth File Transfer",
    "os": "Windows",
    "os_details": "Microsoft Windows 11 Pro 10.0.22621 64-bit",
    "policy_action": "allow",
    "process_name": "python.exe",
    "process_path": "\\??\\C:\\Program Files\\Python312\\python.exe",
    "sub_type": "SUBTYPE_DEVICE_CONTROL",
    "timestamp": 1725847324,
    "type": "endpoint",
    "user": "shubham.singhal@crestdata.ai",
    "record_type": "epdlp",
    "executable_hash": "",
    "location": "",
    "device_sn": "",
    "app": "",
    "destination_file_name": "",
    "printer_identifier": "",
    "file_type": "",
    "dlp_profile_name": "",
    "dlp_profile": "",
    "event_recovered": false,
    "destination_file_path": "",
    "dlp_incident_id": 0,
    "device_name": "",
    "source_file_directory": "",
    "alert_type": "",
    "process_cert_subject": "",
    "policy_name": "",
    "source_file_name": "",
    "incident_id": 0,
    "action": "",
    "policy_name_enforced": "",
    "policy_version": "",
    "executable_signed": false,
    "file_size": 0,
    "justification": "",
    "product_id": "",
    "vendor_id": "",
    "device_id": "",
    "destination_file_directory": "",
    "dlp_rule": "",
    "device": "",
    "alert_name": "",
    "pid": "",
    "port": "",
    "connection_type": "",
    "sha256": "",
    "policy_action_enforced": "",
    "activity": "",
    "driver": "",
    "unc_path": "",
    "file_origin": "",
    "os_user_name": "",
    "md5": ""
}
Create a Client Status Iterator
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/iterator/netskope_ce_cs_iterator?
Method:
POST
Request Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Authorization
Bearer
<v2 token>
Request Parameters
Key
Value
eventtype
clientstatus
Sample API Response – if created successfully [202]
{
"message":"Creation of the iterator, netskope_ce_cs_<unique_id_added> is in progress. Please use the iterator status API to check the status of the iterator. Please note that the iterator name has changed by appending an identifier to ensure uniqueness."
}
Sample API Response – if iterator cannot be created as already exists [400]
{
"message":"Only one iterator is allowed per event type. Please use the existing iterator,<iterator_name>, or delete the existing iterator."
}
Check Status of a Client
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/iterator/
<iterator_name>
Method:
GET
Request Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Authorization
Bearer
<v2 token>
Sample API Response
{
"status": "Ready"
}
Fetch data from a Client Status Iterator
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/iterator/
<iterator_name>
/events
Method:
GET
Request Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Authorization
Bearer
<v2 token>
Request Parameters
Key
Value
operation
next
Sample API Response
_id,as,asn,city,client_install_time,client_version,count,continent,country,device_hash,device_id,enriched,guid,heart_beat,host_info.client_version,host_info.device_make,host_info.device_model,host_info.hostname,host_info.last_update_timestamp,host_info.mac_addresses,host_info.managementID,host_info.nsdeviceuid,host_info.old_nsdeviceuid,host_info.os,host_info.os_version,host_info.serial_number,host_info.steering_config,isp,last_connected_from_private_ip,last_connected_from_public_ip,last_event_timestamp,last_seen_device_event.actor,last_seen_device_event.event,last_seen_device_event.event_details,last_seen_device_event.npa_status,last_seen_device_event.service_name,last_seen_device_event.status,last_seen_device_event.status_v2,last_seen_device_event.timestamp,latitude,longitude,organization,postal_code,region,timestamp,user_info.device_classification_status,user_info.orgkey,user_info.userkey,user_info.username,zipcode,record_type
a7b8a3dd4aa3bebfac869f21,,,,0,123.0.0.2272,1,,,84a3c71061af4152f4e961f9,0AGE55ntv6Lg06dd2F30_092BDAE2-138E-38A4-1BC3-6BC72C4663E8,false,a9981877-c2be-4d8f-bf31-27410d8269d8,false,,"VMware, Inc.","VMware7,1",Win11-50-1-105,1740377213,00:50:56:81:A7:00,,092BDAE2-138E-38A4-1BC3-6BC72C4663E8,AFADEEE3-C9F6-3C54-E215-46EE64F4358C,0,11.0.22621,VMware-42 01 fa 68 fb 6b 7c 57-20 3c 42 df d2 c7 02 32,Default tenant config,,0.0.0.0,,1741034210,0,17,,8,Internet Security,0,0,1741034210,0,0,,,,0,0,lDFAMb4aR2ohwCHthoV,0AGE55ntv6Lg06dd2F30,nilay.modi@crestdata.ai,"396321",clientstatus
1c07aa9d8ad899d02b7c083b,,,,0,123.0.0.2272,1,,,84a3c71061af4152f4e961f9,0AGE55ntv6Lg06dd2F30_092BDAE2-138E-38A4-1BC3-6BC72C4663E8,false,a9981877-c2be-4d8f-bf31-27410d8269d8,false,,"VMware, Inc.","VMware7,1",Win11-50-1-105,1740377213,00:50:56:81:A7:00,,092BDAE2-138E-38A4-1BC3-6BC72C4663E8,AFADEEE3-C9F6-3C54-E215-46EE64F4358C,0,11.0.22621,VMware-42 01 fa 68 fb 6b 7c 57-20 3c 42 df d2 c7 02 32,Default tenant config,,0.0.0.0,,1741034205,0,7,Tunnel Down Due to SSL Error,8,Internet Security,1,0,1741034205,0,0,,,,0,0,lDFAMb4aR2ohwCHthoV,0AGE55ntv6Lg06dd2F30,nilay.modi@crestdata.ai,"396321",clientstatus
Sample API Response Headers
Delete a Client Status Iterator
API Endpoint:
https://
<tenant-url>
/api/v2/events/dataexport/iterator/netskope_ce_cs_iterator_28b7611b-da34-4836-8bdb-89caa3320b6e
Method:
GET
Request Headers
Key
Value
User-Agent
netskope-ce-6.1.0
Authorization
Bearer
<v2 token>
Sample API Response
{
"message": "Successfully deleted the iterator, netskope_ce_cs_iterator_28b7611b-da34-4836-8bdb-89caa3320b6e."
}
Note:
For more details of the iterator, refer to the
documentation
.
User Agent
netskope-ce-6.1.0
Workflow
Generate a v1 token, and/or (preferably) a v2 RBACv3 token for your Netskope tenant.
Configure the Netskope Tenant plugin.
Validate the plugin.
Watch a Video
Click play to watch a video.
Generate a V1 Token
Using a v1 token is not recommended. If required, follow these steps:
In your Netskope tenant, go to
Settings > Tools > REST API v1
.
Click
Generate New Token
.
Click
Generate
.
Click the edit icon located directly beneath the token to adjust the token’s expiration.
By default, the token is generated with no expiry. Choose the expiry duration from the dropdown menu. Select from 30 days, 60 days, 90 days, 180 days, or 365 days.
Click
Save.
Copy the token. It will be required when configuring the Netskope Tenant Plugin in Cloud Exchange.
Generate a V2 (RBACv3) Token
In your Netskope tenant, go to
Settings > Administration > Administrators & Roles
.
Click
Service Account
.
Enter a Service Account Name.
Select a Role for the Service Account.
Note
For Cloud Exchange, a predefined role called
Netskope Cloud Exchange
exists in the Netskope Tenant. This role has all the required permissions to use Cloud Exchange.
Enter an Expire time. Select from Day(s), Hour(s), Week(s), Year(s).
Click
Save
and copy the token. It is required when configuring the Netskope Tenant Plugin in Cloud Exchange.
Configure the Netskope Tenant Plugin
In Cloud Exchange, go to
Settings > Plugin Store
.
Search for and select the
Netskope Tenant v1.6.1
plugin.
Enter a tenant plugin name, tenant URL, and a V1 API token or V2 API token.
Make sure to enter the full tenant URL (like
https://example.de.goskope.com
).
To generate an API token, you can refer to the
Generate a V2 (RBACv3) Token
section.
V1 API token is only needed when sharing Hashes to Netskope.
Click
Save
Troubleshooting the Netskope Plugin
Receiving an Error while Configuring the Tenant
Getting the error:
The Netskope tenant API v2 token does not have necessary permissions configured. Refer to the list of endpoints for which the token is missing permission. *
*
Cause
: The provided v2 token does not have the minimum required permissions to configure the tenant plugin in Cloud Exchange.
What to do
:
Go to
Logging
and look for a warning log similar to the following pattern:
“TENANT Netskope Tenant (Required) [Netskope Tenant]: For **, received 403 error for following endpoint(s)”
Expand the log and get the list of endpoints for which permissions are missing.
Now update the v2 token permissions and add the permission for the shown endpoint.
Receiving a Connection Error. Check the tenant URL and network settings.
Cause
: This error might be occurring either due to an invalid tenant URL, or due to a network connectivity issue of the machine.
What to do:
Validate that the tenant URL starts with
https://
, and it should be the full tenant URL (like
https://example.goskope.com
)
If the tenant URL is correct, validate Cloud Exchange tenant is able to communicate with your Netskope tenant URL.
Rerun the setup script and enter proxy details if required, and the full tenant URL, then check to see if the tenant connectivity check is passed. If the connectivity check is failed, reach out to your IT team.
Receiving an API Token Expired Banner in Cloud Exchange
After configuring Netskope Tenant, you’re seeing
The Netskope tenant API token has expired for <tenant_name>
error. Generate a new token, or re-issue the token, and then update the tenant configuration to resume communication between a Netskope Tenant and Cloud Exchange.
Cause:
This banner is visible due to the V2 token or the RBAC V3 token that you are using is either expired, revoked, or reissued from the tenant.
What to do:
If you are using a V2 token, go to your tenant and check if the V2 token is expired or not. If it is expired, you can change the expiration time. And you can also reissue the token and use it to edit the tenant configuration from
Settings > Netskope Tenants
.
If you are using a RBAC V3 token, same as a V2 token, you can change the expiration time of the token (no need to update in the plugin in this case, as it will be directly be reflected in the existing added token in the config since it was not reissue/revoked). If the token was revoked/reissued, use the new token in the tenant configuration.
After updating the token, the banner will be removed after a successful sync of the plugin.
If the token expired banner appears and the token is not expired, edit the tenant and save without making any changes.
Pulled Alert/Event Count Mismatch from Netskope Tenant for a Specific Time Range During Historical Data Pull
If the count of alerts/events pulled from the Netskope tenant differs from the number available on the tenant for a specific time range during a historical pull, it may be due to that during the historical data pull, the plugin uses
timestamp_hwm
as the pagination marker. In some cases, events were not processed when the
timestamp_hwm
value exceeded the requested
end_time
returned in the Netskope API response. This behavior occasionally resulted in a mismatch between the alert/event counts on the tenant and those pulled into CLS.
What to do:
Update the Netskope Tenant plugin to v1.6.0 in Cloud Exchange v6.0.0 or above.
Receiving Error while Configuring Multiple Plugins
Getting the error:
Error: Value error, Error while creating iterator with name netskope_ce_cs_iterator_**. Cannot create Client Status Iterator. One iterator already exists for the Client Status event for your tenant. Delete the existing iterator to continue.
Cause:
Due to API Limitations of Client Status iterator, creation of more than one iterator is not possible.
What to do:
Users can delete the already existing iterator using API, and create a new one from the plugin.
If a user removes the Client Status event type from one plugin or deletes the Tenant plugin with an iterator, it will automatically delete the iterator from Netskope Tenant. And by configuring a new plugin, users can create an iterator.
For more details on iterator deletion, refer to the
documentation
and reach out to your Netskope tenant support to delete an iterator.
Known Behaviors
While upgrading the tenant plugin, if the user chooses to use the ‘skip’ button then CE will not skip upgrading or will not disable the tenant plugin.
It is recommended to use Netskope Log Shipper v2.3.1 and Netskope Risk Exchange v1.8.0 with Netskope Tenant v1.6.1
It is recommended to configure 1 Tenant plugin per Netskope Tenant. If you are using multiple tenant plugins for the same Netskope tenant then you may encounter errors related to the Client Status iterator while using the Netskope Log Shipper plugin or Netskope Risk Exchange plugin.
It is not recommended to use multiple Netskope Tenant plugins with the same Netskope Tenant. If you have configured Netskope Log Shipper or Netskope Risk Exchange plugin with the Netskope Tenant and you delete the client status iterator then both the plugins will throw error for deleting the Client Status Iterator and you will not be able to use the Netskope Log Shipper or Netskope Risk Exchange plugin.
TENANT Netskope Tenant (Required) [crest-plugin-support]: Error occurred while Deleting Client Status Iterator netskope_ce_cs_iterator_1aef2620-80bc-43b2-ac1d-31d652ee0xxx for tenant https://crest-plugin-support.de.goskope.com.
In this Topic
Netskope Tenant Plugin

---
## (Admin) Browser Set Up
**URL:** https://docs.netskope.com/en/admin-browser-set-up/
**Last Modified:** 2026-02-04T04:18:29+00:00
**Scraped:** 2026-08-02T08:48:19.773658+00:00

(Admin) Browser Set Up - Netskope Knowledge Portal
(Admin) Browser Set Up
Before inviting users to install Enterprise Browser and setting up policies, you must set up the basic configurations for the Enterprise Browser.
Enterprise Browser requires users to authenticate to steer traffic through Netskope to the destination (e.g. the corporate apps). Each request generated by Enterprise Browser needs to include an auth token in the form of a header. Unauthenticated requests are not allowed, and users are prompted to authenticate to their SSO.
Authentication flow to your SSO needs to be bypassed in Enterprise Browser, so your users can effectively authenticate before using Enterprise Browser to access corporate apps.
There are two ways to configure user authentication flow bypass, depending on how you configure conditional access to enforce the use of Enterprise Browser to access your apps.
Option A: Auth (IdP flows) happens outside of Netskope (Browser set up)
Option B: Auth (IdP requests) happen through Netskope IP range / Dedicated Egress IP range
Option A is the default and takes precedence over option Option B.
Option B requires enabling the feature in your account. You must contact Support to enable the feature in your account.
Enterprise Browser Authentication Bypass (Browser Bypass)
This section describes authentication (IdP flows) that happens outside of Netskope,
Option A
noted above. The bypass is configured at the browser level. Enterprise Browser sends the requests directly to the SSO domain. Authentication happens outside of Netskope.This is likely the preferred approach if you want to impose conditional access (Netskope IP range / DEIP)
on each individual corporate app
. Imposing conditional access on all traffic reaching the corporate application is the most secure way to ensure only managed traffic reaches the application, anytime.
Path: Settings → Security Cloud Platform → Enterprise Browser → Browser Setup
Set up the identity provider:
Go to Forward Proxy SAML Section to connect your identity provider with Nestkope’s Forward Proxy. This will allow Netskope to authenticate users using Netskope Enterprise Browser. Select Access Method = “Enterprise Browser”.
Set up the Bypass Settings:
Incoming requests from EB are only accepted after the user is authenticated to the customer’s SSO as configured in the previous step.
You need to specify your IdP domains to allow user authentication to your SSO. If you do not include your IdP domains in this list, users will not be able to reach your IdP Domains to authenticate, and they will not be able to use Enterprise Browser.
E.g. If your IdP is Okta, you will need to include: *.okta.com, *.oktacdn.com each in a separate row.
Include Netskope domains such as: nsauth-<your_tenant_name>.goskope.com and
authservice.goskope.com
. To learn more:
Recommended IdP Bypass List
SAML Proxy Authentication Bypass
This section describes authentication (IdP requests) that happens through Netskope IP range / Dedicated Egress IP range,
Option B
noted above.
Honoring SAML proxy auth bypass in Enterprise Browser is disabled by default (i.e. by default, Enterprise Browser ignores SAML proxy auth bypass settings.)
Honoring SAML proxy auth bypass requires enabling the feature in your account. Contact Support to enable it in your account.
The bypass is configured at the Enterprise Browser / CEP level. Enterprise Browser steers unauthenticated requests to SSO from the Netskope IP range / DEIP range. Authentication requests originate from Netskope.
This is the preferred approach if you want to impose conditional access (Netskope IP range / DEIP)
on the IdP leve
l (e.g. typically with Okta). Imposing conditional access
on all traffic
(Option A) reaching the corporate application is the most secure way to ensure only managed traffic reaches the application, anytime.
Path: Settings → Security Cloud Platform → Forward Proxy → SAML → Settings →Bypass
Recommended IdP Bypass List
The following are the most frequently used IdPs with Netskope Enterprise Browser. This is the minimal bypass lists that need to be configured for the Enterprise Browser for different IdPs in Netskope UI, but it might require adaptations for your specific settings.
EB Bypass List for Microsoft Entra
Explicitly bypass the following domains for Microsoft Entra SSO authentications:
browser.events.data.microsoft.com
autologon.microsoftazuread-sso.com
autologon.microsoft-sso.com
login.live.com
login.microsoftonline.com
login.microsoft.com
aadcdn.msftauth.net
aadcdn.msauth.net
device.login.microsoftonline.com
mysignins.microsoft.com
authservice.goskope.com
nsauth-<tenant-name>.goskope.com
EB Bypass List for Okta
Explicitly bypass the following domains for Okta SSO authentications:
*.okta.com
*.oktacdn.com
authservice.goskope.com
nsauth-<tenant-name>.goskope.com
EB Bypass List for Google Workspace IdP
Explicitly bypass the following domains for Google SSO authentications:
accounts.google.com
play.google.com 
*.gstatic.com
authservice.goskope.com
nsauth-<tenant-name>.goskope.com
EB Bypass List for OneLogin IdP
Explicitly bypass the following domains for OneLogin SSO authentications:
<Domain name in OnLogin>.onelogin.com
web-login-v2-cdn.onelogin.com
cdn.cookielaw.org
cdn.onelogin.com
nsauth-<tenant-name>.goskope.com
In this Topic
(Admin) Browser Set Up

---
## (Admin) User Provisioning
**URL:** https://docs.netskope.com/en/admin-user-provisioning/
**Last Modified:** 2025-08-31T01:45:03+00:00
**Scraped:** 2026-08-02T08:48:20.859547+00:00

(Admin) User Provisioning - Netskope Knowledge Portal
(Admin) User Provisioning
You can invite users to download and install Netskope Enterprise Browser. Configure the style and content of the invitation and installation emails by editing the logo, button color, and templates below.
Enterprise Browser users must exist in your account (e.g. imported via SCIM, AD Importer, etc.) prior to sending invitations.
Path: Settings → Security Cloud Platform → Enterprise Browser → User Provisioning
Provisioning Users:
click the Invite Users button. Select users, user groups or OUs that you want to onboard to use Netskope Enterprise Browser.
Individual invites will be sent using the Email invitation template. You can edit the template and / or use your company logo.
Inviting a user that has been previously invited will resend the onboarding email. License Key remains the same.
The “Do not send onboarding email” option is used in MDM deployment scenarios, where admins need to provision the user in Enterprise Browser  service before running the MDM script.
In this Topic
(Admin) User Provisioning

---
## (Admin) Setting Up Your First RTP Policy for the Enterprise Browser
**URL:** https://docs.netskope.com/en/admin-setting-up-your-first-rtp-policy-for-the-enterprise-browser/
**Last Modified:** 2026-03-02T18:11:01+00:00
**Scraped:** 2026-08-02T08:48:21.960811+00:00

(Admin) Setting Up Your First RTP Policy for the Enterprise Browser - Netskope Knowledge Portal
(Admin) Setting Up Your First RTP Policy for the Enterprise Browser
You can define your own Real-time Protection (RTP) policies with the Enterprise Browser.
Navigate to
Policies
>
Real-time Protection
For Web Access Policies: e.g. you can create a policy blocking any traffic to web sites in a certain category (e.g. “News & Media”). Click “New Policy” → “Web Access”.
You will select
Access Method = Browser”
to apply these policies to “Enterprise Browser” traffic
Leaving Access Method empty will apply to all Access Methods including EB (e.g. “Client”, “GRE”, “Enterprise Browser”…)
For Cloud Apps / DLP Policies: e.g. Admins can create policies to control activities in cloud apps and combine them with DLP profiles to prevent data leakage when EB users interact. E.g.  blocking Downloads of Files with sensitive Data from Google Drive.. Click “New Policy” → “DLP”.
For Private Apps: When users access a browser-based Enterprise Browser private app (for example, an internal HR or time sheet application), their access can be controlled based on configured access control policies. If a matching access policy is in place, Enterprise Browser allows or blocks access accordingly. Click “New Policy” → “Private App Segment Access”.
In this Topic
(Admin) Setting Up Your First RTP Policy for the Enterprise Browser

---
## (Admin) Setting Up Your First Browser Control for the Enterprise Browser
**URL:** https://docs.netskope.com/en/admin-setting-up-your-first-browser-control-for-the-enterprise-browser/
**Last Modified:** 2026-02-27T17:49:58+00:00
**Scraped:** 2026-08-02T08:48:23.085235+00:00

(Admin) Setting Up Your First Browser Control for the Enterprise Browser
You can define Browser Protection policies (copy, paste, print, screenshot/ screen sharing, watermarking) and enforce them in Netskope Enterprise Browser for both SaaS and private applications.
Path: Policies → Enterprise Browser Protection
Select the Users or User groups and the destination to which you want to apply the policy. You can create fine grain policies leveraging Predefined and Custom categories, as well as any cloud application or Cloud App suite (e.g. Create a policy to block, copy, and print in Google Drive).
Admins can use a combination of the following Actions as additional controls to prevent data leakage of sensitive data, to protect internal web apps, and support compliance with data protection regulations.
Actions include:
Copy
– allow or block copying from an application, category, website, or private app
Paste
– allow or block pasting from an application, category, website, or private app
Print
– allow or block printing from an application, category, website, or private app
Screenshot/Screen Sharing
– allow or block capturing content presented in Enterprise Browser corresponding to sensitive applications, categories, website (any destination), or private app
Watermark
– show or hide a watermark which acts as a deterrent, a dissuasive control to prevent users from taking pictures of sensitive data. Apply watermarking to specific website categories, cloud applications, “Any Web” traffic and private applications.
Note:
In the unlikely event of an error while processing Enterprise Browser Protection Policies, the system applies the fallback actions defined by the admin under “Settings”.
Fallback options include:
Copy – block or allow
Paste – block or allow
Print – block or allow
Screenshot/Screen Sharing – block or allow
Watermark – show or hide
Path: Policies → Enterprise Browser Protection → “Settings”
The image below shows the watermark applied on a website. Admins can apply watermarking to specific website categories, cloud applications, application instances, and “Any Web” traffic and private applications.
In this Topic
(Admin) Setting Up Your First Browser Control for the Enterprise Browser

---
## Managing Administrators for RBAC V3
**URL:** https://docs.netskope.com/en/managing-administrators-for-rbac-v3/
**Last Modified:** 2025-10-09T22:19:35+00:00
**Scraped:** 2026-08-02T08:49:04.570234+00:00

Managing Administrators for RBAC V3
The Netskope UI provides full access for deploying and managing admin rights for the Netskope solution. Netskope’s role-based administration enables you to control what different admins can do in the solution. You can delegate responsibilities among admins and granularly control their level of access to the solution to ensure they do not create conflicting policies and settings.
RBAC V3 provides functional controls and uniform authorization for both WebUI and REST API based interactions.
Admins can use automated service accounts without risk of these accounts being able to access the web UI. API access tokens are now issued to a user or a service account (instead of at the tenant level) along with expiry/renewal workflow.
The web admin lifecycle can also be managed more securely by integrating SCIM with the enterprise IdP.
A fully redesigned, next-generation “API First” web UI for identity and access management makes consistent application of roles to human and non-human entities easier than ever before.
Netskope RBAC V3 Overview
Administrators RBAC V3
Roles RBAC V3
Policies RBAC V3
Label Based Access Control (LBAC)
Netskope Advanced Analytics and RBAC V3
In this Topic
Managing Administrators for RBAC V3

---
## Administrators RBAC V3
**URL:** https://docs.netskope.com/en/administrators-rbac-v3/
**Last Modified:** 2025-10-14T18:27:26+00:00
**Scraped:** 2026-08-02T08:49:05.666934+00:00

Administrators RBAC V3 - Netskope Knowledge Portal
Administrators RBAC V3
On the
Settings
>
Administration
>
Administrators & Roles
page >
Administrators
tab, you can see the list of all admins configured for your organization.
Read And Write capability for RBAC V3 roles is only allowed for Tenant Admins. In addition, you cannot apply an IP Allowlist to the Tenant Admin predefined role.
For each admin, you can see the following:
Name
: email or username of the user/invitee.
Status
: displays Active or Pending option based on whether the user has accepted the invitation.
Type
: displays the admin’s type of role (User or Service Account).
Provisioned By
: the user/role type that created the admin user (Local, SCIM, or SAML).
Role
: the admin’s level of access to the functional areas, page permissions, and file access. This is the role chosen which can be a predefined or custom role.
API Credential
: displays the status of the REST API Token, date the token expires, option to generate/change/revoke the token.
MFA
: displays the status, Disabled/Enabled.
Last Login
: date and time of the user’s last login.
Auth
: the method by which the admin was authenticated, e.g. API Key, etc.
Ellipses
: click to edit/disable the admin, generate/change/revoke the token, or delete the user from the administrators list.
You can
filter
the admin list by:
Name
Role
Provisioned By (Local, SCIM, or SAML)
Type (User Account or Service Account)
Clicking
Clear all filters
clears the filter selections and clicking
Clear and remove all filters
clears the selections and removes the filters from the Filters bar view.
Tenant Admins
In Role-Based Access Control (RBAC) V3, a
Tenant Admin
has the highest level of administrative permissions within their tenant/account, including the ability to manage other administrators and roles. However, when a user attempts to create or clone a role, the permission
“Administration > Admins > Manage”
is intentionally disabled for all roles other than the core
Tenant Admin
role.
This is a critical security feature designed to prevent privilege escalation.
The Purpose of the Security Control
The primary reason for this behavior is to maintain a secure and robust RBAC framework. The ability to manage other administrators and roles is a unique privilege reserved exclusively for the pre-defined
Tenant Admin
role. This restriction is a fundamental principle of the RBAC V3 design and applies to all user-created or cloned roles, not just those derived from the Tenant Admin role.
Here’s why this security control is in place:
Preventing Privilege Escalation:
If any user can create a new role and grant the ability to manage other admins and roles, it would create a potential loophole. A malicious actor can create a new role with this permission and then use it to create new users or roles with even higher privileges, effectively bypassing the security controls. This allows them to grant full administrative access to unauthorized users.
Maintaining a Secure Hierarchy:
The RBAC V3 model is designed with a clear and secure hierarchy. The Tenant Admin role acts as the root administrator for the tenant/account. Allowing other, potentially less-controlled roles to manage admins would compromise this structure and make it difficult to track and control administrative permissions.
Ensuring the Integrity of the RBAC System:
By restricting the “Manage” permission to the original Tenant Admin role, the system ensures that the fundamental controls for user and role creation remain in a trusted and uncompromised state. This prevents a user with a non-standard or cloned role from rendering the RBAC controls ineffective.
Expected Behavior
The only predefined role that has
“Administration > Admins > Manage”
permission is the
Tenant Admin
.
When any other role is created or cloned, the
“Administration > Admins > Manage”
permission will be
grayed out and disabled
. This is a deliberate design choice to protect against privilege escalation.
This design ensures that only the designated Tenant Admin can perform critical functions like creating new roles and managing user accounts, thus protecting the integrity of the entire system.
Local User Account
Click
Settings
to access the Local User Account page.
Max Failed Login Attempt
: specify the minimum number of log in attempts that can be allowed before the admin user is locked out of the UI. The minimum is three log in attempts
Idle Timeout
: set how often a session times out, minimum is 5 minutes and the max is 60 minutes.
Password Expiration
: set how often a password expires.
Allow concurrent logins by the same admin
: select the checkbox to disallow concurrent log ins by the same admin. This means if an admin logs in from a second browser instance, they will be logged out from their first browser session.
Verification Link Validity
: set how many hours and/or minutes the verification link is valid.
Migrating Local and SSO Users
In some cases, you may have a local and SSO user with the same email address. If you have a user that has both a local login and SSO login, after migrating to RBAC V3, the ‘provisioned by’ will be
Local
. The role that shows in the Role column in the UI is the role that was assigned to the local user.
The SSO role is assigned and managed by the IdP. If a local user was disabled before the migration, its status will be preserved, and a password reset will be required to re-enable it.
REST API Auth Settings
Click
Settings
to access the REST API Auth Settings page.
Your options include via
API Key
.
Or via
OAuth 2.0
Invite a New Admin
Navigate to the
Settings
>
Administration
>
Administrators & Roles
page >
Administrators
tab > click
Invite
The Invite page appears.
Ensure roles exist before assigning to or creating an admin.
Type the email of the new administrator. Ensure the email domain for the new administrator is part of the Admin Account Domains.
Select a Role from the dropdown list. Tip: ensure the role exists prior to inviting admins.
Optionally, enable MFA for the admin.
Click Done.
Netskope will send a verification email with an account activation URL.
The new admin user can change the password during the account verification process.
The user will receive a second email with the one-time password (OTP) to add in addition to changing their password.
The admin account will be activated once the account verification is complete.
Go to Settings to configure the verification time period. Users will receive a verification link via email when the admin creates or resets passwords for a local account. You can define how long the verification link is valid. The minimum is 15 minutes and the maximum is 72 hours.
Create a New Service Account
Service accounts enable admins to create non-interactive admin accounts to use with REST APIs.
Navigate to the
Settings
>
Administration
>
Administrators & Roles
page >
Administrators
tab > click
Service Account
The New Service Account page appears.
Ensure roles exist before assigning to or creating a Service Account.
Type the name of the service account.
Select a Role from the dropdown list. Tip: ensure the role exists prior to creating a service account.
Optionally, you can generate a REST API Token and set the expiration by number of days.
Optionally, select the checkbox to generate the token later.
Click
Create
.
To generate the token later from step 4 above, navigate to the Administrators list page and click the ellipsis at the end of the row.
Understanding Authentication
for Service Accounts
You will not see an “Enable multi-factor authentication” (MFA) option for accounts with the
Service Account
role. This is by design.
Admin Accounts
are used by humans to log in to the user interface. They authenticate with an email and password, and can have MFA enforced as an additional security layer for that interactive login.
Service Accounts
are non-interactive. They are designed for programmatic access to the Netskope API and
do not
log in to the UI. Instead of a password and MFA, they authenticate using a secure, revokable
API token
.
Because service accounts do not have a password and cannot log in to the UI, traditional MFA is not applicable. Security is maintained through the proper management and safeguarding of their API tokens.
In this Topic
Administrators RBAC V3

---
## DSPM Sidecar Administration Overview
**URL:** https://docs.netskope.com/en/dspm-sidecar-administration-overview/
**Last Modified:** 2026-06-19T21:05:35+00:00
**Scraped:** 2026-08-02T08:51:17.959505+00:00

DSPM Sidecar Administration Overview - Netskope Knowledge Portal
DSPM Sidecar Administration Overview
Overview
This article explains how to manage Netskope DSPM sidecars. Sidecars are deployed in groups called sidecar pools, which link to your Netskope tenant using a unique security token. This page covers how to create and manage these pools and tokens within the Netskope UI.
Additionally, you can deploy a Single Appliance that bundles both the sidecar and DLP services into one virtual machine. To learn more:
Deploy the DSPM Single Appliance
.
For an overview of how sidecars and DLP appliances fit into the DSPM architecture, see
DSPM Architecture
. For firewall and egress requirements, see
Firewall Settings for DSPM-Hosted Instances
.
Sidecar Administration UI
Go to
DSPM
>
Administration
>
Sidecar
to access the Sidecar Administration page.
This page displays the following components:
License Key
: Appears at the top of the page with a copy button. You use this key during appliance deployment.
+ ADD SIDECAR POOL
: Creates a new sidecar pool for the standalone deployment model.
+ ADD SINGLE APPLIANCE
: Launches the wizard to deploy a Single Appliance.
The
Sidecar Pools
table lists all registered pools and includes the following columns:
Column
Description
Sidecar Pool Name
The name assigned to the pool.
Status
The health status of the pool (
green
= Healthy,
yellow
= warning,
grey
= Incomplete).
DLP Version
The DLP appliance version linked to the pool.
Sidecar Version
The sidecar software version running in the pool.
Host Name
The appliance identifier and serial (e.g.,
Single_appliance
or
Dlpod_appliance
).
Actions
Options to edit, view details, or delete the pool. If actions are missing, the pool belongs to a Single Appliance and is system-controlled.
Register a Sidecar Pool (Distributed Deployment Only)
To establish the connection between your sidecars and your Netskope DSPM tenant, you first generate a unique authentication token by registering a sidecar pool. If you already have an existing sidecar pool token, you can skip this procedure.
Go to
DSPM
>
Administration
>
Sidecar
.
Click
+ ADD SIDECAR POOL
.
In the
Details
tab, enter a descriptive
Name
for the pool.
Click
Save
.
When the Sidecar Authentication Token window appears, click
Copy
.
(Note: You need this token for the installation process).
Click the
x
to close the window.
Since you
haven’t
yet associated this token with a deployed sidecar, the new pool appears only if you click the
Show Inactive Sidecars
icon.
Install and Associate Sidecars (Distributed Deployment Only)
After you register a sidecar pool and copy the authentication token, deploy the sidecar instances in your environment. The deployment process varies depending on your environment (cloud or on-premises) and the specific installation method.
Follow the detailed instructions in the appropriate guide below:
Deploy a DSPM Sidecar on AWS EC2 via Terraform
Deploy a DSPM Sidecar on AWS EC2 via CloudFormation
Deploy DSPM Sidecars via Helm Chart
Deploy a DSPM Sidecar on GCP via Cloud Run
Deploy a DSPM Sidecar on Azure via Container Instances
Retrieve Required Keys for the DLP Appliance (Distributed Deployment Only)
The DLP appliance requires two separate keys. You retrieve both within the Netskope console:
REST API v1 Key
: The appliance leverages this key to fetch the latest DLP configurations. This key may already exist in your environment; if so, you can reuse it. Otherwise, generate a new one:
Go to
Settings
>
Tools
>
Rest API v1
.
Click
Generate New Token
.
Set the expiration to
never expire
.
License Key
: The appliance setup leverages this key to validate the DLP entitlement. The Netskope console generates this key automatically, and it appears at the top of the
DSPM
>
Administration
>
Sidecar
page.
Link a DLP Appliance to a Sidecar Pool (Distributed Deployment Only)
Before deploying sidecars, you must have a DLP appliance available in the same network. For prerequisites and deployment instructions, see
Deploy the DLP Appliance for DSPM
.
Each sidecar pool must link to a DLP appliance for data classification. A single DLP appliance can serve multiple sidecars, as long as their sidecar pools register to the same appliance address.
To link the appliance:
Navigate to
DSPM
>
Administration
>
Sidecar
.
Click the
Edit
icon for the pool associated with the sidecar you just deployed.
Select the DLP appliance from the
DLP Appliance
drop-down.
Note:
If the DLP appliance
isn’t
listed, manually enter its IP address)
Click
Test Connection
to validate the configuration.
If you receive a successful test message, click
Save
.
Edit a Sidecar Pool (Distributed Deployment Only)
You can edit the name of a registered sidecar pool at any time.
Go to
DSPM
>
Administration
>
Sidecar
.
Find the sidecar pool you want to edit.
Click the
Edit
icon.
Make your changes in the Edit Sidecar Pool window.
Click
SAVE
.
View Sidecar Pool Details
Click a sidecar pool name to view its details. The details panel displays the following information:
Pool Information
, which includes the pool name, status (
Active
or
Inactive
), and an
Edit Pool
link
DLP Appliance Information
, which displays the host name and serial number, DLP version, IP address, uptime, memory usage, and average CPU load
Sidecar(s)
, which provides a table listing all sidecars in the pool with their name, status, version, last seen date, creator, and creation date
Upgrade and Schedule (Single Appliance Only)
For pools created by a Single Appliance, the details panel also displays upgrade management options.
Automatic Upgrade Schedule
shows the current schedule, the next automatic upgrade date, and provides an
Upgrade Now
link for on-demand upgrades.
Single Appliance Upgrade History
is a table showing past upgrades, including the status (
Completed
,
Cancelled
), timestamp, trigger (
Auto update
,
Manual
), and description (e.g.,
Full Upgrade, v135.0.24
).
To modify the schedule:
Click
Edit Schedule
in the pool details panel.
Choose when to apply the upgrade after release (
Within the first week after release
,
Within the second week after release
, or
Within the third week after release
).
Select the day of the week and start time (in the appliance’s local timezone).
Click
Save Schedule
.
In this Topic
DSPM Sidecar Administration Overview

---
## Platform Administration & Identity
**URL:** https://docs.netskope.com/en/platform-monitoring-and-administration/
**Last Modified:** 2026-04-16T01:39:38+00:00
**Scraped:** 2026-08-02T08:52:11.522707+00:00

Platform Administration &amp; Identity - Netskope Knowledge Portal
Platform Administration & Identity
Update the Company Profile in DSPM
Netskope DSPM Licensing
Manage DSPM Administrator Permissions (RBAC)
Integrate Microsoft Entra ID with DSPM
Integrate Okta Universal Directory with DSPM
Manage DSPM Service Accounts
Map Employees to DSPM Usernames
View DSPM Activity Logs
Export DSPM Logs to Amazon S3
In this Topic
Platform Administration &amp; Identity

---
## Manage DSPM Administrator Permissions (RBAC)
**URL:** https://docs.netskope.com/en/manage-dspm-administrator-permissions-rbac/
**Last Modified:** 2026-02-06T05:19:28+00:00
**Scraped:** 2026-08-02T08:53:59.301394+00:00

Manage DSPM Administrator Permissions (RBAC) - Netskope Knowledge Portal
Manage DSPM Administrator Permissions (RBAC)
Overview
This article explains how to manage administrator access to Netskope Data Security Posture Management (DSPM) screens and functions using Role-Based Access Control (RBAC) v3. You can grant permissions by assigning pre-defined roles or by creating custom roles with granular control over DSPM-specific functional areas.
Understand DSPM Functional Areas
Access to DSPM is divided into four functional areas. When creating a custom role, you can assign
Manage
or
View
permissions to each of these areas.
Functional Area
Controlled DSPM Screens and Features
Reporting
Dashboard
Alerts
Reports
User Assessment
Management
Data Stores > Data Store Inventory
Data Stores > Configuration Analysis
Data Stores > Privileges Analysis
Classification > Classification Management
Classification > Entity Data Types
Classification > Data Tags
Policies > Policy Management
Policies > Policy Categories
Policies > Workflows
User Identity > Employee Management
User Identity > User Tags
Administration
Administration > Infrastructure Connections
Administration > Integrations
Administration > Notification Settings
Administration > Sidecar
Sampling
Controls two separate functions:
- Classification Management > Fields > Fetch Samples button
- Classification Management > Files > Get Snippets button
Screens not explicitly listed above (e.g., Licensing, Support) are accessible by any role that has general access to the DSPM module.
Permissions for Pre-Defined Roles
The following table outlines the default DSPM permissions for the standard, pre-defined RBAC v3 roles.
Manage:
The administrator can view and perform all actions within the functional area.
View:
The administrator can only view information and cannot make changes.
None:
The administrator has no access to the screens within the functional area.
Pre-Defined Role Name
Reporting
Management
Administration
Sampling
Tenant Admin
Manage
Manage
Manage
View
Delegated Admin
Manage
Manage
None
View
Restricted Admin
Manage
View
None
None
Cloud Intelligence Analyst
Manage
None
None
None
Application Risk Analyst
Manage
None
None
None
Enterprise Applications Admin
Manage
None
None
None
Directory Admin
Manage
None
None
None
Security Admin
Manage
Manage
None
View
InfoSec Operations Admin
Manage
Manage
None
View
Compliance Officer
Manage
View
None
None
Security Analyst
Manage
None
None
None
IaaS and PaaS Admin
Manage
Manage
None
None
NS Technical Success
Manage
View
None
None
NS Technical Support
View
View
View
View
Netskope Cloud Exchange
None
None
None
None
Configure a Custom Role for DSPM
You can create a custom role to grant specific combinations of DSPM permissions.
Go to
Settings > Administration > Roles
.
Click
New Role
or select an existing custom role to edit.
In the
Permissions
section, enable the
parent functional area
to see the DSPM permissions
>
Select the checkbox for
Security Posture > Data
.
Scroll down to the new
DSPM
section
>
Using the dropdowns, grant
Manage
,
View
, or
None
for each of the four DSPM functional areas (Reporting, Management, Administration, Sampling).
Click
Save
.
Non-Applicable RBAC Features
When configuring custom roles specifically for DSPM, be aware that the following RBAC v3 functionalities do not apply to DSPM permissions:
Scope
Obfuscation
IP Allowlist
In this Topic
Manage DSPM Administrator Permissions (RBAC)

---
## (Admin) Setting Up Your First Extensions Governance Security Policy
**URL:** https://docs.netskope.com/en/admin-setting-up-your-first-extensions-governance-security-policy/
**Last Modified:** 2025-10-23T05:08:24+00:00
**Scraped:** 2026-08-02T08:54:46.851132+00:00

(Admin) Setting Up Your First Extensions Governance Security Policy - Netskope Knowledge Portal
(Admin) Setting Up Your First Extensions Governance Security Policy
This feature is in Controlled GA. Contact your Netskope Sales Representative to enable this feature in your account.
We are introducing
Extension Management capabilities for Enterprise Browser
, empowering administrators with greater control over browser extensions. This feature enables admins to create comprehensive extension management policies at the account level.
With this feature, administrators can:
Define Default Actions:
Set a default action to either allow or block all extensions from the Chrome Web Store.
Create Exception Allow Lists:
Specify lists of allowed extensions using their unique Extension IDs.
Force-Install Extensions:
Automatically install a subset of designated extensions for all users within the account.
Navigate to
Policies
>
Enterprise Browser Protection
>
Extension Governance
The list page displays.
When no policies are configured the default configuration for extension management applies which is to block all extensions.
You can only have one Extension Governance policy for your account. Once you’re baseline policy is created, the New Policy button is grayed out. However, you can edit your baseline policy.
1.Click
New Policy
to create an Extension Governance policy.
2. Click
+Extension
in the Exception List to search for an extension name or ID. Anything you add in this field is allowed at your user’s discretion to install (#1 in the image above).
3. Click
+Extension
in the Force Install List to search for an extension name or ID. Anything you add in this field will be force installed for all users (#2 in the image above).
By default this baseline policy is enabled.
4. Click
Save
.
In this Topic
(Admin) Setting Up Your First Extensions Governance Security Policy

---
## Configure your Netskope Tenant for Custom File Classification File Hash Sharing (Beta)
**URL:** https://docs.netskope.com/en/configure-your-netskope-tenant-for-custom-file-classification-file-hash-sharing-beta/
**Last Modified:** 2025-11-14T02:31:04+00:00
**Scraped:** 2026-08-02T08:55:19.339905+00:00

Configure your Netskope Tenant for Custom File Classification File Hash Sharing (Beta) - Netskope Knowledge Portal
Configure your Netskope Tenant for Custom File Classification File Hash Sharing (Beta)
To share file hashes between your Netskope tenant and Custom File Classification in Cloud Exchange, you need to:
Configure a trainable file classifier in your Netskope tenant for Custom File Classification to send file hashes for use in Real-time policy.
While setting up Custom File Classification for file hash sharing, you will get a list of all the classifier names in a dropdown with the classifiers you previously configured in your Netskope tenant.
When you have file hashes going to your Netskope tenant, you will need to build a policy to leverage this new data source. In this workflow, the file hashes will be used to enhance Netskope Real-time Protection.
Configure a DLP Profile on a Netskope Tenant (Beta)
Configure a Real-time Protection Policy using the DLP Profile on Netskope Tenant (Beta)
Configure Custom File Classification Sharing with your Netskope Tenant Classifier (Beta)
Configure Trainable File Classifier on a Netskope Tenant (Beta)
In this Topic
Configure your Netskope Tenant for Custom File Classification File Hash Sharing (Beta)

---
## Configure Trainable File Classifier on a Netskope Tenant (Beta)
**URL:** https://docs.netskope.com/en/configure-trainable-file-classifier-on-netskope-tenant-beta/
**Last Modified:** 2025-11-14T01:32:01+00:00
**Scraped:** 2026-08-02T08:55:20.450164+00:00

Configure Trainable File Classifier on a Netskope Tenant (Beta) - Netskope Knowledge Portal
Configure Trainable File Classifier on a Netskope Tenant (Beta)
Log in to your Netskope Tenant.
Go to
Policies > DLP
.
Click
File Classifiers
and then
New Trainable File Classifier
.
Enter a File Classifier Name, select a threshold, and upload at least 20 positive training files to create the classifier successfully.
When done, it will take some time to activate the classifier.
In this Topic
Configure Trainable File Classifier on a Netskope Tenant (Beta)

---
## Configure Custom File Classification Sharing with your Netskope Tenant Classifier (Beta)
**URL:** https://docs.netskope.com/en/configure-custom-file-classification-sharing-with-your-netskope-tenant-classifier-beta/
**Last Modified:** 2025-11-14T01:05:54+00:00
**Scraped:** 2026-08-02T08:55:21.557717+00:00

Configure Custom File Classification Sharing with your Netskope Tenant Classifier (Beta) - Netskope Knowledge Portal
Configure Custom File Classification Sharing with your Netskope Tenant Classifier (Beta)
You need to get the sharing information from Custom File Classification to use later when setting up a profile in the Netskope tenant. This information is in the Custom File Classification module when you created a file hash share with a Netskope tenant as the Destination Configuration. You must have a Netskope Custom File Classification plugin and a sharing rule in order to share File Hashes for training for your Netskope tenant.
If you haven’t already done so, go to
Custom File Classification > Sharing
to create a sharing configuration to use in your Netskope tenant. The Sharing configuration settings needed are:
Source Configuration
: Select a source configuration, any 3rd-party platform pulling the File data.
Destination Configuration
: Select Netskope Custom File Classification plugin as destination.
Target
: Netskope CFC supports one target action, sharing CFC hashes, which will be auto selected in the Target field.
Map Fields
:
Business Rule
: Select the Business Rule from the ones configured.
File Classifier
: Contains a dropdown with all the available File Classifiers present on the configured Netskope Tenant.
Training Type
: Positive/Negative. Positive training data helps train the model to identify files that are similar to the ones being uploaded. Negative training data helps train the model to identify what is not considered a match to the classifier’s model.
In this Topic
Configure Custom File Classification Sharing with your Netskope Tenant Classifier (Beta)

---
## Partner Access (Accessing Private Apps in other Tenants)
**URL:** https://docs.netskope.com/en/partner-access-accessing-private-apps-in-other-tenants/
**Last Modified:** 2025-12-19T21:10:09+00:00
**Scraped:** 2026-08-02T08:56:14.956845+00:00

Partner Access (Accessing Private Apps in other Tenants) - Netskope Knowledge Portal
Partner Access (Accessing Private Apps in other Tenants)
Partner Access allows users to access Private Applications across multiple Netskope tenants (such as Managed Service Providers, partners, third-party organizations, or multi-tenant organizations) without needing to unenroll or uninstall the Netskope Client, or leveraging clientless access through a browser.
A Partner Tenant is defined as the external tenant from which a end-user might be able to connect to. Users can seamlessly switch between their Primary Tenant and authorized Partner Tenants via the Netskope Client UI.
Key Benefits
Multi-tenant access:
Seamlessly switch between partner organizations to access authorized private resources.
No re-installation required:
Eliminates the need to unenroll/reinstall the Netskope Client when switching tenants.
Unified Security:
While accessing a Partner’s private apps, Internet Security policies remain enforced by the Primary Tenant.
Prerequisites
Before configuring Partner Access, please review the following requirements:
Supported OS:
Windows, macOS.
Enrollment Method:
Prelogon and VDI tunnel users are unsupported in partner tenants.
Steering:
Dynamic Steering configuration is not supported in partner tenants. Ensure partner users are matched to a steering configuration
without
Dynamic Steering in the partner tenant.
Partner Requirements:
The Partner Tenant must have a Forward SAML proxy configured for Client enrollment and must provide the appropriate authentication credentials to the user.
Upcoming Enhancements
In Netskope Client version R134, we will introduce the following improvements:
Secure Configuration Service:
Currently partner tenants that utilize the Secure Configuration Service to encrypt the Netskope Configuration are not supported. In the next software release, we will introduce support for Secure Configuration Service, which requires administrators to share an Encryption Token with end-users in order to store, read, and write the encrypted configuration.
MacOS External Browser Support:
We will introduce support for the External Browser in MacOS for clients that are installed with the appropriate install parameters in the next software version. This means the Netskope Client will authenticate partner tenants in the same way as the primary tenant.
Availability:
This feature is currently in
Controlled General Availability
. Contact Netskope Support or your Sales Representative to enable this feature for your tenant.
Configure Partner Tenants (Admin Workflow)
Connect to Third-Party Tenants (User Workflow)
Operational Behavior and Validation
In this Topic
Partner Access (Accessing Private Apps in other Tenants)

---
## Configure Partner Tenants (Admin Workflow)
**URL:** https://docs.netskope.com/en/configuring-partner-tenants-admin-workflow/
**Last Modified:** 2026-01-26T22:51:25+00:00
**Scraped:** 2026-08-02T08:56:16.062848+00:00

Configure Partner Tenants (Admin Workflow) - Netskope Knowledge Portal
Configure Partner Tenants (Admin Workflow)
To enable users to switch to a partner tenant, the administrator of the
Primary Tenant
must configure the partner details in the Client Configuration.
Note:
This configuration is applied in the tenant
from where
the users are connecting (the Primary Tenant). It is not bi-directional automatically.
Go to
Settings > Security Cloud Platform > Netskope Client > Client Configuration
.
Open the relevant Client Configuration and click
Private App Segment
.
Enable the
Partner Tenant Access
checkbox.
Enter the Partner Details:
Tenant Name:
Enter a display name for the tenant (like
Partner 1
).
Tenant URL:
Enter the partner’s tenant URL (like
partner1.goskope.com
).
Click
+ADD
to include additional partner accounts (Maximum of 20).
Click
Save
.
In this Topic
Configure Partner Tenants (Admin Workflow)

---
## Connect to Third-Party Tenants (User Workflow)
**URL:** https://docs.netskope.com/en/connecting-to-third-party-tenants-user-workflow/
**Last Modified:** 2025-12-20T00:13:21+00:00
**Scraped:** 2026-08-02T08:56:17.174068+00:00

Connect to Third-Party Tenants (User Workflow) - Netskope Knowledge Portal
Connect to Third-Party Tenants (User Workflow)
Terminology
Primary Tenant:
Your main Netskope tenant handling Internet Security policies.
Partner Tenant:
The external tenant providing access to specific private applications.
Scenario 1: Switching from the Primary to a Partner Tenant
When a user switches from their Primary organization to a Partner organization:
The User selects the specific
Partner Tenant
(e.g., Org C) from the Client UI menu.
A new enrollment window opens.
The User enters the authentication credentials specific to Org C.
Upon success, the User can access Private Apps hosted by Org C.
Scenario 2: Switching between Partner Tenants
If a user is already connected to Partner Org C and needs to switch to Partner Org B:
The User selects Org B in the Client UI.
A pop-up appears confirming the unenrollment from Org C.
The user clicks
Continue
.
The user enters the credentials for Org B to complete the IDP enrollment.
Access to Org B’s Private Apps is granted.
Scenario 3: Switching back to the Primary Tenant
To return to the default state:
User selects the
Primary Tenant
(Org A).
A pop-up window appears confirming the tenant switch.
The client reverts to the Primary Tenant’s context.
In this Topic
Connect to Third-Party Tenants (User Workflow)

---
## Manage Global Attributes in the Tenant UI
**URL:** https://docs.netskope.com/en/manage-global-attributes-in-the-tenant-ui/
**Last Modified:** 2026-02-18T04:05:53+00:00
**Scraped:** 2026-08-02T08:57:32.383851+00:00

Manage Global Attributes in the Tenant UI - Netskope Knowledge Portal
Manage Global Attributes in the Tenant UI
Certain product features for NPA can now be enabled directly in the Tenant UI. You can view and modify selected NPA Publisher feature flags in the Global Attributes window.
Go to
Settings > Security Cloud Platform > Publishers
.
In the top-right corner of the page, click
Global Attributes
.
Review the available features to use, enable those you want, and then click
Save
.
In this Topic
Manage Global Attributes in the Tenant UI

---
## Admin Console
**URL:** https://docs.netskope.com/en/admin-console/
**Last Modified:** 2025-09-01T12:42:42+00:00
**Scraped:** 2026-08-02T09:02:43.112069+00:00

Admin Console - Netskope Knowledge Portal
Admin Console
The Netskope Admin console, or
tenant
, provides the ability to use all the Netskope products and services in one location. Starting with administrative functions, like tenant access and privileges, to viewing informative dashboards, managing incidents, using Skope IT to monitor activity, assess app risk and advanced analytics, and create reports.
App Catalog
Manage
Administration
Netskope UI and Dashboard
Incidents
In this Topic
Admin Console
