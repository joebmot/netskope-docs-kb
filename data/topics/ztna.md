# Netskope Docs — Ztna
_Generated: 2026-09-03 11:43 UTC_
_Pages: 92_

---
## Deploy the Netskope Client for Netskope Private Access
**URL:** https://docs.netskope.com/en/deploy-the-netskope-client-for-netskope-private-access/
**Last Modified:** 2026-05-26T21:44:42+00:00
**Scraped:** 2026-09-03T10:43:05.111817+00:00

Deploy the Netskope Client for Netskope Private Access - Netskope Technical Documentation
Deploy the Netskope Client for Netskope Private Access
Netskope Private Access recommends that the Netskope Client to be installed on a
Windows
,
MacOS
,
iOS
,
Android
, or
Chrome OS
device. The Client steers Private Access application traffic to Private Access gateways. An alternate method is to use
Browser Access
for Netskope Private Access.
Important
When the Client detects an alternate steering method, like a GRE or IPSec tunnel, it disables the Client-based data tunnel (TLS tunnel) to the Netskope platform and therefore access to private apps. This configuration can be useful for disabling private app steering while on-premises.
The Netskope Client supports these
operating systems and platforms
.
Note
See the
Netskope Client Interoperability
topic to learn more about Netskope Client compatibility with third-party apps.
Install the Client for Private Access
Partner Access (Accessing Private Apps in other Tenants)
Use the NPA Client in Windows Multi-User Virtual Desktop Environments
View Private Access Status for Devices
Allow Users to Disable Private App Segment Access on the Netskope Client
Windows Autopilot with Private Access Prelogon
Configure Client Prelogon Connectivity
Use Client Re-authentication
CGNAT Address Support for Local DNS Resolution
In this Topic
Deploy the Netskope Client for Netskope Private Access

---
## Install the Client for Private Access
**URL:** https://docs.netskope.com/en/install-the-client-for-private-access/
**Last Modified:** 2026-08-31T17:36:25+00:00
**Scraped:** 2026-09-03T10:44:44.963758+00:00

Install the Client for Private Access - Netskope Technical Documentation
Install the Client for Private Access
After adding users, the users receive an email with links to download the Client. The user must choose either the macOS, Windows, Android, iOS, or Chrome OS Client download. You must install version 65 or later of the Netskope Client to use Netskope Private Access.
After receiving the email, the user needs to click the link for the appropriate platform for their device.
When the download is complete, the user can install the Client.
The Client should automatically start and show that it’s connected.
Tip
The Client will register with the Netskope Private Access backend and will be ready to steer traffic.
Verify the Client is Steering a Private App
Open a browser (or another client application).
Try to access the private app. (Example:
http://jira.site.io:22
).
The user should be able to access it.
Disable the Netskope Client.
Try to access the private app. The user shouldn’t be able to access it.
Enable the Netskope Client again.
In this Topic
Install the Client for Private Access

---
## Netskope Private Access for Microsoft Active Directory Domain Services
**URL:** https://docs.netskope.com/en/netskope-private-access-for-microsoft-active-directory-domain-services/
**Last Modified:** 2026-03-03T02:37:43+00:00
**Scraped:** 2026-09-03T10:45:43.227344+00:00

Netskope Private Access for Microsoft Active Directory Domain Services - Netskope Technical Documentation
Netskope Private Access for Microsoft Active Directory Domain Services
This article explains how to configure Netskope Private Access (NPA) applications for Microsoft Active Directory Domain Services, such as DNS, Kerberos, and WINS.
Often customers are looking for the same end-user experience in using Windows Active Directory Domain Services for mobile workforce as for on-premises. For example, if users working remotely on a company-managed Active Directory Domain joined device would like to connect to an on-premises application which uses Windows integrated authentication, they should not be prompted for a password.
Netskope Private Access enables administrators to expand Domain Services experience to the remote users conveniently and securely.
Configure Private Apps for DNS with the Publisher DNS Feature Enabled
The first step to enable end-users using Active Directory Domain Services and file shares remotely is to configure native,
pass-through
DNS resolution for the internal Active Directory Domain. In the default Netskope Private Access deployment, each private application is represented to the client with an artificial non-routable IP address that’s been returned to the user in the DNS query response.
For example, if an on-premises private application has an IP address 10.0.0.10, the NPA Publisher will be accessing it using this IP address, while the end-users will receive an artificial IP address like 191.1.1.5 when running a DNS query from their managed devices. To use Windows Domain Services, users have to use the real IP addresses of Windows Domain Controllers. To achieve this you need to configure a Private Application for DNS with the Publisher DNS feature enabled. This private DNS application allows users to join Active Directory Domains, query Active Directory groups policies, and FSMO roles from their remote devices.
Architecture Considerations
Deploy a Publisher per Data Center/Cloud collocated with the Active Directory servers.
For every Active Directory Domain (like
example.com
,
apac.example.com
,
europe.example.com
) in the Forest will require an
<Active Directory DNS>
and an
<Active Directory Domain>
Private App definition (per the example Private App definitions in the following procedure) mapped to the correct Publisher based on their location.
To create a Private App definition, log in to the Netskope UI, and go to
Settings > Security Cloud Platform > App Definition > Private Apps
. Create two new Private App definitions, one for Active Directory DNS and one for Active Directory Domain.
Create a Private App to provide access to Directory DNS. In this case,
domain.local
is your local domain. Click
New Private App
and enter these parameters:
Application Name: Enter a name, like Active Directory DNS. (or what every you prefer).
Host: Enter these hosts:
*._http.
domain.local
*._https.
domain.local
*._kkdcp.
domain.local
*._msdcs.
domain.local
*._tcp.
domain.local
*._udp.
domain.local
*._sites.
domain.local
TCP: Enter
53
.
UDP: Enter
53
.
Publisher: Select the Publisher(s) that can access your local internal DNS server resources.
Use Publisher DNS: Enable this toggle.
Click
Save
.
Create a Private App definition that enables users to access Windows Domain Controllers from their managed devices.
Because the previous application you configured will return to the end-user internal IP address of the domain controller, you need to configure a private application that encompasses IP addresses for all domain controllers so that they become accessible via Netskope Private Access. Click
New Private App
and enter these parameters:
Application Name: Enter a name like Active Directory Domain (or whatever you prefer).
Host: Enter the FQDN and IP of every Active Directory server colocated at the same site as the Publisher.
TCP: Enter
53,88,135,137,139,389,445,464,636,1512,3268,3269,5357,49152-65535
.
UDP: Enter
53,88,123,135,137,138,389,464,1512,5357,49152-65535
Publisher: Select the Publisher colocated with the AD server.
Use Publisher DNS: Enable this toggle.
Click
Save
.
Create new Private App Access policy using the criteria specific to your environment. Go to
Policies > Real-time Protection
, edit an existing policy, or click
New Policy
and select
Private App Access
.
Enter the parameters using the criteria specific to your environment.
Source: Select whatever is appropriate.
Destination: Select
Private App
, and then select the Private App definitions you created (per this example, Active Directory DNS and Active Directory Domain).
Profile & Action: Select
Allow
.
Set Policy: Enter a name for the policy (whatever you prefer).
Status: Enable this toggle.
Click
Save
.
Click
Apply Changes
.
Active Directory Port Definitions
Port Number
Protocol(s)
Service Description
53
TCP/UDP
DNS
88
TCP/UDP
Kerberos
123
UDP
NTP / Time
135
TCP
RPC Endpoint Mapper
389
TCP/UDP
LDAP / CLDAP
445
TCP
CIFS / SMB
464
TCP/UDP
Kerberos Password Change
636
TCP
LDAPS
3268
TCP
Global Catalog LDAP
3269
TCP
Global Catalog LDAPS
9389
TCP
ADWS (used by Powershell)
49152-65535
TCP
High Ports for RPC
In the above configuration:
Host remote device will be accessing domain controllers using domain SRV records
_gc._tcp.
<yourwindowsdomain.com>
and
_ldap._tcp._sites.DomainDnsZones. yourwindowsdomain.com
, so we’re defining the windows underscore zones and forest and domain DNS zones with a wildcard FQDN to cover all DNS queries for Windows Domain Services, as shown in the screenshots earlier.
Port: Port 53 should be used for the DNS traffic.
Enabling SCCM with Netskope Private Access
If you’ve already deployed Publishers in ideal locations for accessing SCCM resources, your first step is to ensure that you’ve followed the best practices for deploying
Active Directory
services via Netskope Private Access.  This ensures services like Kerberos, SRV resolution, and other services are available for proper SCCM authentication and selection.
If Active Directory is properly configured, then you can configure SCCM over NPA by following the process below:
Define Boundary Groups based on Active Directory Sites using the Publisher IPs or RFC 1918 subnets.
Define Application Definitions for SCCM resources.
Create Real-time Protection Policies to enable access to SCCM resources.
To learn more, go to:
SCCM and Products: Netskope Private Access
.
In this Topic
Netskope Private Access for Microsoft Active Directory Domain Services

---
## Netskope Private Access for SMB and DFS Services
**URL:** https://docs.netskope.com/en/netskope-private-access-for-smb-and-dfs-services/
**Last Modified:** 2026-01-24T01:02:36+00:00
**Scraped:** 2026-09-03T10:45:44.344816+00:00

Netskope Private Access for SMB and DFS Services - Netskope Technical Documentation
Netskope Private Access for SMB and DFS Services
This article explains how to configure Netskope Private Access (NPA) applications for file sharing protocols such as Server Message Block (SMB) and Distributed File System (DFS).
SMB is a communication protocol for providing shared access to files, network browsing, printing and inter-process communication over a network. There are a few well-known SMB protocol implementations like CIFS and Samba. SMB protocol relies on lower-level transport protocols like TCP and UDP. SMB works through a client-server approach, where the client makes specific requests and the server responds accordingly. Traditional file sharing resources can be accessed by SMB protocol in the form of
\FileServer1Tools
or
\FileServer2Tools
as an example.
DFS provides the ability to logically group distributed SMB file sharing resources and transparently link them into a hierarchical namespace. For example, instead of browsing through individual file sharing resources, the client accesses
\YourWindowsDomainPublicSoftware
and gets transparently redirected into either
\FileServer1Software
or
\FileServer2Software
, depending on its proximity and availability.
Here are descriptions of different elements that make up a DFS namespace:
Namespace server: A namespace server hosts a namespace. The namespace server can be a member server or a domain controller.
Namespace root: The namespace root is the starting point of the namespace. In the above example, the name of the root is Public, and the namespace path is
\YourWindowsDomainPublic
. This type of namespace is a domain-based namespace because it begins with a domain name and its metadata is stored in Active Directory Domain Services (AD DS).
Folder: Folders without folder targets add structure and hierarchy to the namespace, and folders with folder targets provide users with actual content. When users browse a folder that has folder targets in the namespace, the client computer receives a referral that transparently redirects the client computer to one of the folder targets.
Folder targets: The folder target is where data and content is stored. In the previous example, the folder named Tools has two folder targets –
\FileServer1Software
and
\FileServer2Software
.
The vast majority of SMB implementations are tightly integrated with Windows Active Directory authentication services like Kerberos or NTLM. Kerbersos protocol is the primary authentication and authorization method for accessing file sharing resources. In order to access certain resources, the client retrieves a Kerbeos ticket from the Active Directory Domain Controller, which is acting as Key Distribution Center (KDC). This ticket is carried by the SMB protocol and presented to the destination file sharing service, which in turn validates it with KDC too. The NTLM protocol might be used as a fallback in case Kerberos is not supported by legacy or not domain-joined clients.
In case of distributed deployment when SMB file sharing resources and/or DFS namespace servers are configured on separate servers hosted in separate sites, you need to create separate configurations associated with different Publishers in order to achieve even traffic distribution.
Proper deployment for Active Directory Domain Services (which includes Kerberos) is documented in this
article
and it
must
be followed as a prerequisite if the domain-joined endpoints need to access DFS/SMB shares. Certain use cases with non-domain joined devices and/or legacy clients may rely on NTLM authentication. In this situation, connectivity to Active Directory domain controllers is not required, but the primary application to resolve internal domain resources with the Publisher DNS option from that article should still be created and assigned to the users in addition to the configuration below.
To create a Private Application, log in to the Netskope UI, go to
Settings > Security Cloud Platform > App Definition > Private App Segments
, and then create a new Private App Segment named File Sharing Site 1 with these parameters:
Host (as per example in above diagram):
10.0.1.30
10.0.1.40
Browser Access toggle is disabled.
Protocol and Port:
TCP: 135, 137, 139, 445
UDP: 137, 138, 389, 443, 445
Publisher: In this case, you select
pub1
because it is dedicated for file sharing services and best positioned to serve traffic to those resources. If you have more than one publisher deployed at that physical location, you can also add them to the list of publishers serving this application for redundancy purposes.
Use Publisher DNS toggle is disabled.
Click
Save
.
Repeat the same steps to create another new Private App Segment named File Sharing Site 2, but use
10.0.2.30
as the IP address for the Destination, and
pub2
for the Publisher, and then click
Save
.
Ports used in the above configuration:
Port
Description
TCP: 135
RPC communication
TCP: 137
NetBIOS session service
TCP:139
NetBIOS session service
TCP:445
SMB over TCP without NetBIOS
UDP:137
SMB over UDP (name services)
UDP:138
SMB over UDP (Datagram)
UDP: 389
LDAP Directory, Replication, User and Computer Authentication, Group Policy, Trusts
UDP: 443
Add this port if a server has SMB over QUIC enabled. This is per guidance provided
here
.
UDP: 445
SMB over UDP without NetBIOS
Note
The above configuration is intended to provide backward compatibility to older versions of SMB protocol and clients (i.e. pre-Windows 2000). Modern SMB implementations require only TCP:445 to be configured in addition to Active Directory Domain Services connectivity mentioned above. We recommend that you evaluate connectivity requirements as it pertains to legacy SMB protocols and consider removing TCP:139, UDP: 137, UDP: 138 ports from your configuration to prevent network over-exposure.
After defining the above File Sharing applications, you can assign them to a desired users and/or groups in a Real-time Protection policy to provide ZTNA-based access to your SMB/DFS resources.
In this Topic
Netskope Private Access for SMB and DFS Services

---
## Private Access Best Practices
**URL:** https://docs.netskope.com/en/private-access-best-practices/
**Last Modified:** 2026-01-27T02:05:27+00:00
**Scraped:** 2026-09-03T10:46:37.013663+00:00

Private Access Best Practices - Netskope Technical Documentation
Private Access Best Practices
Consider these best practices when using Netskope Private Access.
Best Practice for Managing Publisher Recovery and Migrations
This section provides recommended best practices for managing Netskope Private Access (NPA) Publisher recovery and migration efforts.
The Publisher, as deployed, does not contain any sensitive or persistent info that needs to be maintained and preserved separately outside of the management plane. In order to be connected to the Netskope tenant, a Publisher needs to be registered with a unique registration code.
Sometimes you may be faced with the situation where you need to rebuild or recover the Publisher. Some of those situations include:
Losing/misplacing Publisher user password or certificate.
Having hosting hypervisor or storage device experience hardware failure or disk corruption.
Desire to migrate a Publisher to a newer version of the operating system.
Due to the nature of Publishers architecture and configuration, it is not worth trying to recover any existing Publisher images, but rather deploy a new Publisher image and register it under the same Publisher definition. We recommend that if you ever experience failure or loss of access to the Publisher, do the following:
Build and deploy a brand new Publisher in the same location as the failed/degraded Publisher.
Ensure that the failed/degraded Publisher is shut down, and verify this by looking at the Publisher in the Netskope tenant to confirm it shows as
Disconnected
in the Netskope UI:
Click on the menu icon
to the right of the publisher and click
Edit
.
Click
Save
.
Click
Generate Token
. If the button is grayed out, the Publisher is still connected to the tenant and you need to ensure it is in the
Disconnected
state before proceeding.
Copy the token and use it to register the new publisher that you have built.
After performing the steps above, your new publisher will automatically take on the role and definition of the old one and will begin serving applications that the old publisher was assigned to.
Best Practice for Using the Publisher DNS Feature in Netskope Private Access
This section explains how to properly use the Use Publisher DNS feature in a Private App Segment App Definition. First, let’s revisit how NPA works with this feature turned off.
When you define a destination on the Private App Segment and assign that app to a user via a policy, NPA on the endpoint listens for any DNS name queries and, if any of them matches the Private App hostname, NPA resolves them to a fictitious IP address. In previous versions the IP address range was
191.x.x.x
, but in the current versions we use a CGNAT address space of
100.64.0.0/16
(let’s call it a stub IP address). Then, when a process is making a request to that stub IP address, the NPA intercepts it, tunnels it to a Publisher, and the Publisher performs a new name resolution based on the DNS servers it points to in order to resolve the internal IP of the published application.
When you turn on Use Publisher DNS, the concept of using a stub IP addresses goes away. The actual DNS request for the hostname specified in the request is captured and tunneled over to the Publisher, and the response received by the Client is the actual IP address returned by the DNS query to the DNS servers that Publisher points to.
For example, if you are trying to access the Private App Segment
portal.company.com
, and that hostname resolves to
10.10.10.10
by the Publisher’s DNS server, the IP address returned to the endpoint process (like a browser) is going to be
10.10.10.10
instead of the stub IP address (
191.x.x.x
, or
100.64.0.0/16
, depending on the version). The browser is then making a request to the IP address
10.10.10.10
, which is as arbitrary as any IP address can be and NPA needs to know that it should intercept and tunnel traffic destined to that IP address. This is why you need to include either a CIDR block covering the IP address of the private application, or the exact IP address of the private application, in the Private App Segment App definition.
Note
The IP address and CIDR block need to be on separate lines. For example:
hosta.company.com
10.10.10.10/32
A CIDR notation (like
/32
) is not needed if you specify an exact IP host.
This approach tells NPA on the endpoint that it needs to intercept traffic destined to
10.10.10.10
and send it over the NPA tunnel.
This is a very powerful concept, but it requires you to exercise due diligence in identifying the exact private IP space that should be served by a particular application. If you accidentally specify a broader range than should be handled by a single application, then you may inadvertently send traffic to all of the private apps that have the Use Publisher DNS flag switched on to a single publisher or publisher group defined on the application that covers the IP range and not via the Publisher the app hostname is defined on. For a practical example of best practice deployment with Publisher DNS mode, please refer to the NPA
guide.
Approaches to Managing and Defining Private App Segments
If you are defining applications with the Use Publisher DNS feature, you have a couple of options. One is to ensure that each Private App Segment App Definition includes an appropriate CIDR range that corresponds to the hostnames being resolved. If you’re publishing multiple applications, such an approach may become tedious as you’d want to ensure that for each application, the CIDR range specified is unique and non-overlapping with other apps definitions to avoid the steering conflict of where to send that traffic.
Another way to approach this is to define Private App Segment App Definitions by CIDRs that are served through the same [set of] publishers. Let’s look at the following scenario.
You are defining three private applications:
hosta.company.com
,
hostb.company.com
, and
hostc.company.com
, all reachable by the
same
publisher. You know that the CIDR network range of the Publishers serving those three application is
172.16.0.0/16
, but you’re not sure of the specific IPs of each app, or those IPs can change in the future.
Configuration Approach
You can define three separate applications with just their respective hostnames/ports with the Use Publisher DNS feature turned on. Then you also create a private application for
Location A
network, as an example, and define it by CIDR
172.16.0.0/16
with the Use Publisher DNS feature turned off. This will ensure that NPA will intercept any traffic destined to the
172.16.0.0/16
networks and application port[s] that you define and send it over the NPA tunnel. The CIDR definition does not need to be a part of the same private app definition that is using the Use Publisher DNS feature. Refer to the table below for visual representation of how the application definitions would look like:
App Name
Host
Port
Use Publisher DNS
App A
hosta.company.com
TCP/443
Yes
App B
hostb.company.com
TCP/443
Yes
App C
hostc.company.com
TCP/443
Yes
Location A
172.16.0.0/16
TCP/443
No
This configuration will allow you to access
App A
,
App B
, and
App C
by hostname, as well as any internal resource defined by the
Location A
CIDR block. You can also see that
Location A
application CIDR definition may result in undesired steering actions as it covers a very broad RFC1918 range that may interfere with the local network resources, and steering conflicts or irregularities may occur. Defining a private app by such a CIDR block exposes all of its IP addresses to access by the user whom this app is assigned to, potentially violating the least privilege tenet of the Zero Trust Network Access (ZTNA) concept.
The most secure way of defining private applications with the Use Publisher DNS feature is to provide precise CIDR-based IP definitions for the private apps in their definition. For example, in defining private app A, you should put in hostname
hosta.company.com,
and, if it resolves internally to
10.10.10.10
, you should put
10.10.10.10/32
as the CIDR value in that app definition. Then in defining private app B, you put in hostname
hostb.company.com
, and, if it resolves internally to
10.10.10.11
, you put
10.10.10.11/32
as the CIDR value in that app definition as well. This approach allows you to effectively prevent accidental overexposure to the internal network or creating network IP conflicts. Please refer to the table below for the recommended private app definitions in order to achieve this goal:
App Name
Host
Port
Use Publisher DNS
App A
hosta.company.com 10.10.10.10/32
TCP/443
Yes
App B
hostb.company.com 10.10.10.11/32
TCP/443
Yes
App C
hostc.company.com 10.10.10.12/32
TCP/443
Yes
Considerations for Assigning Private App Segment App Definitions in a Real-time Protection Policy
For individual users, NPA supports access to an unlimited number of Private Apps regardless of the application specification in a Private App Definition. Each Private App Segment App Definition is referenced by an Application Segment Name (
1
). In an App Definition, the Destination specifications (
2
) can be either individual IP addresses or IP subnets, hostnames, or wild card domains (
*.corp.com
).
Private App Segment App Definitions are enumerated in a Real-time Protection policy to enable end-user access to Application Segment specifications. Based on policy definitions, for each user, NPA builds a logical association of Application Segment specifications, and supports up to a maximum of 6000 Application Segment specifications. For more than 6000 application specifications per user, you should consider aggregating IP addresses, or hostnames into IP subnets, or wild card domains.
An administrator needs to ensure that Real-time Protection policy for any user does not exceed 40 MB. The size of the Real-time policy for any user can be seen in the output of the NPA Troubleshooter tool.
Note
The
NPA Troubleshooter tool
displays the Application Segment specifications and size of the Real-time policy for a specific user.
In this Topic
Private Access Best Practices

---
## Private Access Troubleshooting
**URL:** https://docs.netskope.com/en/private-access-troubleshooting/
**Last Modified:** 2026-03-24T00:06:56+00:00
**Scraped:** 2026-09-03T10:46:38.140816+00:00

Private Access Troubleshooting - Netskope Technical Documentation
Private Access Troubleshooting
This document is designed to help troubleshoot issues with end-users connecting to private applications using Netskope Private Access (NPA). NPA is a Zero Trust Network Access connection that is a secure alternative to traditional VPNs.
This guide assumes that you have:
Installed a publisher in your data center or public cloud environment.
Enabled Private Apps in your steering configuration.
Created a private app and assign it to a Publisher.
Created a Real-time Protection policy to allow the user/group/OU access to the private app.
The Troubleshooter is built into the Netskope UI, and most of the errors you may encounter are covered in the following sections with suggestions on how to resolve them.
Go to
Manage a Publisher
to learn about troubleshooting Publisher logs, using SNMP and Linux commands to monitor resources, and more.
The NPA Troubleshooter Tool
General Troubleshooting Methods
Troubleshooting NPA Allowlisting for Specific Domains in AWS
Troubleshooting Performance and Connectivity using TCPing and PsPing
Troubleshooting Performance and Connectivity using Ping, Traceroute, or Telnet
Troubleshooting Why NPA-steered Websites are Inaccessible
What Do the Private Access Device Status Types Mean?
In this Topic
Private Access Troubleshooting

---
## Private Access REST APIs
**URL:** https://docs.netskope.com/en/private-access-rest-apis/
**Last Modified:** 2026-01-22T22:07:06+00:00
**Scraped:** 2026-09-03T10:46:39.330131+00:00

Private Access REST APIs
This topic explains how to use the new REST API v2 pages in the Netskope UI for Private Access Publishers and Private Apps.
Netskope REST APIs use an auth token to make authorized calls to the API. Netskope REST APIs provide access to resources via URI paths. The token must be used in every REST API call for the tenant. The token can be created for use with specified APIs in the Netskope UI by going to
Settings
>
Administration
>
Administrators & Roles
>
Administrators
and clicking
Service Account
.
Create a New Token
The workflow to create a token has changed. For instructions to create a new token, go
here
.
Swagger API Documentation
To see API parameters information, click the
API Documentation
link on the REST API v2 page or in the Create REST API Token dialog box, which opens the Swagger UI. Available endpoints, methods, and parameters are displayed.
To view endpoint payload information in Swagger:
Click on one of the endpoints, like
infrastructure
, to see the parameters available. The
infrastructure
endpoints are used for the Publisher APIs.
The
steering
endpoints are used for the Private Apps APIs.
Parameter descriptions provide information about the available values, format requirements, and factors related to use with other parameters. Some parameters provide dropdown lists for supported options, other parameters use text field entries.
Copy the endpoint Request URL and parameters to use in your API calls. Make sure the token is added to the Netskope-Api-Token header before sending requests; otherwise, you will get an error.
Publisher APIs
List of APIs
Create a Publisher:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/createNPAPublishers
Get a Publisher:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/getNPAPublisherById
Get a list of Publishers:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/getNPAPublishers
Update a Publisher:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/replaceNPAPublisherByID
Patch a Publisher:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/updateNPAPublisherById
Delete a Publisher:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/deleteNPAPublishers
Get the Publisher Alerts conﬁguration:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/getNPAPublisherAlerts
Update the Publisher Alerts conﬁguration:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/createNPAPublisherAlerts
Trigger the Bulk Update Publisher action:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/triggerNPAPublisherUpdates
Get the List of Publisher Releases:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/getNPAPublisherObjects
Get all Private Apps associated to a Publisher:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/getNPAPublisherApps
Generate and retrieve a Publisher Registration token:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/generateNPAPublisherToken
API Parameters
Key
Type
Example
Description
apps_count
integer
3
Total Private Apps associated with Publisher.
common_name
string
e2eabac9e9f715ff
Unique name gets generated for a Publisher.
connected_apps
List
List [ "[Cloud Exchange]", "[WebServer]" ]
List of Private Apps connected to a Publisher.
id
integer
6
Publisher ID.
lbrokerconnect
boolean
false
Publisher Local Broker connection status.
name
string
pub1.local
Name of the Publisher.
publisher_upgrade_profiles_id
integer
1
ID of the Publisher upgrade profile.
adminUsers
List [string]
List [ "admin1@abc.com ", "admin2@abc.com " ]
List of users present in the admin section.
eventTypes
string (Enum)
List [ "CONNECTION_FAILED", "UPGRADE_STARTED" ]
List of event types generated by the Publisher.
selectedUsers
string
abc@xyz.com,def@xyz.com
Additional users who need the events of Publishers.
Publisher Upgrade Proﬁle APIs
List of APIs
Create a Publisher Upgrade Proﬁle:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/createNPAPublisherUpgradeProfile
Get a Publisher Upgrade Proﬁle:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/getNPAPublisherUpgradeProfile
Get a List of Publishers Upgrade Proﬁles:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/listNPAPublisherUpgradeProfiles
Put a Publisher Upgrade Proﬁle:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/updateNPAPublisherUpgradeProfile
Delete a Publisher Upgrade Proﬁle:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/deleteNPAPublisherUpgradeProfile
Update a Publisher Upgrade Proﬁle to a Set of Publishers:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/BulkupdateNPAPublishers
API Parameters
Key
Type
Example
Description
docker_tag
string
8690
Unique tag for each release present in docker.
enabled
boolean
true
Status of the Publisher upgrade profile.
frequency
string
0 0 1 * TUE
Specifies the date time and month.
id
integer
10
The unique Publisher profile ID.
publisher_upgrade_profiles_id
integer
1
External ID of the Publisher profile.
name
string
My Upgrade profile
Name of the Publisher profile.
release_type
string
Latest
Mentions different Publisher build availability.
timezone
string
US/Eastern
Time zones selection.
Private Apps APIs
List of APIs
Create a Private App:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/post_api_v2_steering_apps_private
Get a Private App:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/get_api_v2_steering_apps_private_private_app_id_
Get a list of Private Apps:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/get_api_v2_steering_apps_private
Update a Private App:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/put_api_v2_steering_apps_private_private_app_id_
Patch a Private App:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/patch_api_v2_steering_apps_private_private_app_id_
Delete a Private App:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/delete_api_v2_steering_apps_private_private_app_id_
Get the Policy In Use for Private Apps:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/post_api_v2_steering_apps_private_getpolicyinuse
API Parameters
Key
Type
Example
Description
token
string
"token":"
<your_token>>
"
Required. Obtain the REST API token from your Netskope tenant. To learn how to generate a token, go to
Create a New
Token
.
We recommend that you place the token in the request header, not in the endpoint URL.
app_name
string
"app_name": "
<application_name>
"
Required. Name of the Private App(s).
host
string
"host":"host.com"
Required. Enter an FQDN, wildcard domain, IP subnet, or IP address.
publishers
array
"publisher_id":"office-hq"
"publisher_name":"of ice-private-apps"
Required. The name and/or ID of the Publisher that provides access to this application.
private_app_id
string
"private_app_id":"office-365"
Required. The ID of the Private App being accessed.
protocols
array
"type":"tcp"
"port":"80"
"ports":"80,8010-8050"
Required. Deﬁnes the protocol type and port(s). Type values are TCP or UDP.
private_app_protocol
boolean
"private_app_protocol":"https"
Optional. Protocol used by the Private App. Values are HTTP or HTTPS.
clientless_access
boolean
"clientless_access": true
Optional. Enables Browser Access for Private Apps. Values are true or false. Default is false.
use_publisher_dns
boolean
"use_publisher_dns": true
Optional. Enables the Publisher DNS option. Values are true or false.
Default is false.
trust_self_signed_certs
boolean
"trust_self_signed_certs": true
Optional. Enable if Trusted self-signed certiﬁcates should be used for Browser Access. Values are true or false. Default is false.
fields
string
“fields: id, name, host}
Optional. Returns the speciﬁed ﬁelds in the JSON object for the GET method.
silent
boolean
"silent": 1
Optional. Shows status code but skips data code. Values are 1 (true) or 0 (false).
Default is 0.
is_user_portal_app
boolean
true
Status of the user portal app.
allow_unauthenticated_cors
boolean
false
Status of the CORS.
uri_bypass_header-value
string
X-NSKP-URIBYPASS
URI bypass header.
bypass_uris
[string]
["/1/", "/2/",... "/20/"]
List of URIs to be bypassed.
app_option
{}
Currently not in use. Ignore.
(Optional) Option used by RDP/SSH.
tags
String [{tag_id, tag_name}]
[{tag_id, tag_name}]
List of Private app tags
real_host
string
www.use-fqdn.com
Host used mostly for browser access based.
NPA Real-Time Policy APIs
List of APIs
Create an NPA Real-Time Policy:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/policy/post_api_v2_policy_npa_rules
Get an NPA Real-Time Policy:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/policy/get_api_v2_policy_npa_rules_id_
Get NPA Real-Time Policies:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/policy/get_api_v2_policy_npa_rules
Patch an NPA Real-Time Policy:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/policy/patch_api_v2_policy_npa_rules_id_
Delete an NPA Real-Time Policy:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/policy/delete_api_v2_policy_npa_rules_id_
API Parameters
Key
Type
Example
Description
description
string
This is a NPA real time policy.
Policy description. This value currently doesn’t show up in the Netskope tenant.
enabled
string
policy_name
Status of the real time policy.
group_id
string
1
Policy group ID.
group_name
string
policy_group
Policy group name.
rule_data
npa_policy_rule_data
Example too large to show.
Structure of the real-time policy.
access_method
[string] Enum [Client, clientless]
[Client]
It can be client or clientless based.
dlp_actions
{actions, dlp_profile}
{“Allow”, “Payment Card”}
Actions for DLP feature
actions
String Enum: allow, block, alert, quarantine, bypass
[“allow”]
One of the enums to be selected.
dlp_profile
string
“Payment Card”
These are predefined profiles.
tss_actions
{action_name, Remediation_profile, Severity, template}
{
Action_name: “allow”,
Remediation_profile: “None”,
Severity: “medium”
}
Actions for TSS feature.
action_name
string Enum: [block, alert, allow]
[“alert”]
One of the enums to be selected.
remediation_profile
string
“profile_remedy”
Not Applicable for NPA.
severity
string Enum: [low, medium, high]
[medium]
One of the Enums to be selected.
template
string
Default template or Custom template
Name of the block template created for user notification.
tss_profile
[string]
Default profile or custom profile
Scanning profile for Threat protection profile.
json_version
integer
3
(Optional) It’s a fixed value and will not change.
device_classification_id
[integer]
[45]
List of device classification IDs.
match_criteria_action
string action_name Enum [allow, block]
[“allow”]
RT policy action name.
policy_type
string “private-app”
“private-app”
This is fixed and will not change.
privateAppTagIds
List [string]
List [“1”,“2”]
List of tag IDs.
privateAppTags
List [string]
List [“tag1”,“tag2”]
List of Private App tags.
privateApps
List [string]
List [“app1”,“app2”]
List of Private App names.
privateAppsWithActivities
File Activities with size and type.
[
{
"activities": [
{
"activity": "any",
"list_of_constraints": []
}
],
"appName": "[172.31.12.135]"
}
]
/code>
Applicable to TSS and DLP.
userGroups
List [string]
[“user/group1/group2”]
List of group users.
userType
string Enum: [user]
[“user”]
This is fixed and will not change.
users
[user]
[“user@netskope.com”]
List of available users can be added.
organization_units
List[string]
List [“engineering/qa”]
List of OUs can be added.
rule_name
string
npa-policy-name
Real-time policy name.
rule_order
npa_rule_order
{order,position, rule_id,rule_name}
Structure for the rule_order where the new policy to be placed.
order
string Enum: [top, bottom, before, after]
“top”
Position where real-time policy needs to be placed.
position
integer
5
(Optional) Existed rule order value.
rule_id
integer
1
Existed rule ID of the policy.
rule_name
string
policy-name
Existed policy name in rule order.
NPA Policy Groups APIs
List of APIs
Create NPA Policy Groups:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/policy/post_api_v2_policy_npa_policygroups
Get an NPA Policy Group:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/policy/get_api_v2_policy_npa_policygroups_id_
Get NPA Policy Groups:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/policy/get_api_v2_policy_npa_policygroups
Patch NPA Policy Groups:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/policy/patch_api_v2_policy_npa_policygroups_id_
Delete NPA Policy Groups:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/policy/delete_api_v2_policy_npa_policygroups_id_
API Parameters
Key
Type
Example
Description
group_id
integer
4
Policy group ID.
group_name
string
npa-policy-group
Name of the policy group.
group_order
It’s a structure.
{group_id: 1, "Order": before|after}
Group order structure.
group_id
string
"1"
Group ID reference of existing group.
order
string
"before|after"
Position where new group to be placed.
NPA Discovery Settings APIs
List of APIs
Create NPA Discovery Settings:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/post_api_v2_steering_apps_private_discoverysettings
Get NPA Discovery Settings:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/get_api_v2_steering_apps_private_discoverysettings
API Parameters
Key
Type
Example
Description
host
List [string]
[“www.netskope.com”, “10.31.13.12”]
List of FQDNs and IPs can be provided.
organization_units
List [string]
[“org/qa”]
List of Org units.
publishers
{publisher_id, publisher_name, publisher_cn}
{“132”,“netskope_publisher”, “d48fb11de337a0 f”}
List of Publishers.
publisher_id
string
“132”
Unique ID of the Publisher.
publisher_name
string
netskope_publisher
Publisher name.
publisher_cn
string
d48fb11de337a0f
Publisher common unique identifier.
status
string Enum: [“ENABLED”, “DISABLED”]
ENABLED
Status of the app discovery.
users
List [string]
[“abc@netskope.com”]
List of Users.
userGroups
List [string]
[“users/group1”]
List of User groups.
NPA Private App Publishers Association APIs
List of APIs
Update a Publisher:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/put_api_v2_steering_apps_private_publishers
Patch a Publisher:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/patch_api_v2_steering_apps_private_publishers
Delete a Publisher:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/delete_api_v2_steering_apps_private_publishers
API Parameters
Key
Type
Example
Description
private_app_ids
List [string]
[“1”, “48”]
List of Private App IDs to be provided.
publisher_ids
List [string]
[“56”, “69”]
List of Publisher IDs to be provided.
NPA Private App Tags APIs
List of APIs
Create Private App Tags:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/post_api_v2_steering_apps_private_tags
Get a Private App Tag:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/get_api_v2_steering_apps_private_tags_tag_id_
Get a list of Private App Tags:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/get_api_v2_steering_apps_private_tags
Update a Private App Tags:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/put_api_v2_steering_apps_private_private_app_id_
Patch a Private App Tag (Bulk Private App update):
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/patch_api_v2_steering_apps_private_tags
Delete a Private App Tag:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/delete_api_v2_steering_apps_private_tags_tag_id_
Delete a Private App with Tag Association:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/delete_api_v2_steering_apps_private_tags
Get number of policies in use for private app tags:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/post_api_v2_steering_apps_private_tags_getpolicyinuse
Update the private app tags based on the tag ID:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/steering/put_api_v2_steering_apps_private_tags_tag_id_
API Parameters
Key
Type
Example
Description
id
string
“23”, “13”
This is the Private App ID.
tags
{[tag_name]}
[{“tag1”},{“tag2”}]
Format expected.
tag_name
string
“tag1”
Name of the tag.
ids
[string]
[“2”, “5”]
List of the Private App IDs.
Local Broker APIs
List of APIs
Create a Local Broker:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/post_api_v2_infrastructure_lbrokers
Get a Local Broker:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/get_api_v2_infrastructure_lbrokers id_
Get a list of Local Brokers:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/get_api_v2_infrastructure_lbrokers
Update a Local Broker:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/put_api_v2_infrastructure_lbrokers_id_
Delete a Local Broker:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/delete_api_v2_infrastructure_lbrokers_id_
Create a Local Broker Hostname Conﬁg:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/post_api_v2_infrastructure_lbrokers_brokerconfig
Update a Local Broker Hostname Conﬁg:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/put_api_v2_infrastructure_lbrokers_brokerconfig
Get a Local Broker Hostname Conﬁg:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/get_api_v2_infrastructure_lbrokers_brokerconfig
Generate and Retrieve the Local Broker Registration Token:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/post_api_v2_infrastructure_lbrokers_id_registrationtoken
Check if the Name provided is a Valid Duplicate or not:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/get_api_v2_infrastructure_npa_namevalidation
Validate the Resource based on resourcetype:
https://
<tenant-URL>
/apidocs/?include_beta_routes=1#/infrastructure/post_api_v2_infrastructure_npa_resource_validation_resourcetype_
API Parameters
Key
Type
Example
Description
name
string
localbroker1
Name of the Local Broker.
common_name
string
d48fb11de337a0f
Local broker common name
id
integer
45
Unique ID of the Local Broker.
registered
boolean
true
Status of the Local Broker registration.
hostname
string
www.localconnect.com
FQDN of the Local Broker DNS.
In this Topic
Private Access REST APIs

---
## Private Access FAQs
**URL:** https://docs.netskope.com/en/private-access-faqs/
**Last Modified:** 2026-06-04T23:11:59+00:00
**Scraped:** 2026-09-03T10:46:40.452486+00:00

Private Access FAQs - Netskope Technical Documentation
Private Access FAQs
Can Netskope Private Access co-exist with other VPN clients?
Netskope supports the following deployment model for Netskope Private Access in the presence of another VPN client on the user’s device.
The Netskope Private Access tunnel in the Netskope Client can actively forward traffic, provided the VPN client is disabled, and the VPN tunnel is not actively intercepting and/or forwarding traffic to Private Apps (including DNS).
Is there any order that the Client uses to match hosts defined in Private Applications? If you have subnets, subdomains, wildcards and hosts, what is the order that the Client will try to use to match the traffic?
The vertical order of matching the rules is:
Host or IP (without any wildcard)
Subnet (CIDR)
Subdomain
The horizontal order is not guaranteed except for subdomains, which matches the longest prefix first.
A horizontal order example is:
App1: 10.10.0.0/23
App2: 10.10.0.0/24
App3: myserver.mydomain
Subnet: App1, App2 are in the same level, and thereby horizontal
Subdomain: App3
The gateway/client will find App1 and App2 first, and then App3.
What services and polling interval does a Publisher use to check if a private app/service is available?
The polling interval is about 1 minute.
The Publisher will try to connect to a configured port on a Private App to check whether the private app is reachable.
Important factors to consider:
The Publisher works best when you define Private App by hostname (like
jira.globex.io
) and port (like
8080
).
When a Private App is specified with a port range, the Publisher will use only the first port from the range to check availability. For example, port range 70-90 will return unreachable, even if you are listening on port 80, because the only port that will be checked is 70 (this is a known limitation).
If an app definition specifies ports and/or port ranges, it will check whether any of them are reachable. For example, if you specify 22, 70-90, if it’s able to reach port 22, it will mark the app as reachable.
The Publisher can’t check reachability for Private Apps that are defined with a wildcard (
*.globex.io
) or CIDR block (
10.0.1.0/24
).
How do I return to the setup menu during a Publisher SSH session?
From the
/home/ubuntu
folder, enter
sudo ./npa_publisher_wizard
.
How does Netskope  handle the connection of an application when the end user terminates a session?
Netskope will terminate the end-to-end tunnel between the Publisher and the end application upon session termination in SSH and other TCP-based flows.
Do Publishers support Active-Active in the event there are multiple Publishers that have access to the same Private App?
Publishers work in Active-Active mode. Active-Active mode enables higher throughput. Up to 16 publishers are supported in an Active-Active deployment per app. Further details on Publisher Selection can be found
here
.
What happens if the Publisher registration token is corrupted during the initial deployment stage? Can I reset it locally at the Publisher?
If the registration failed (for example, because you missed a digit from the registration code), you can SSH into the Publisher and provide a new registration token.
If the registration succeeded, but you decided to register the Publisher with another token, this is not officially supported and not advised. You will need to reinstall the Publisher.
My 2nd (or subsequent) Publisher shows as Connected to an older publisher record in the Netskope UI. Now what?
This could be a known issue. If you copied your new Publisher from an older (working) Publisher, then you’ve likely hit this issue. For example, creating an AMI image from a known working EC2 instance, and then launching a new instance from that AMI image, is an example of one way to hit this issue.
Please contact Netskope Support or create a new Publisher rather than copying an AMI or image.
How much bandwidth can a Publisher handle?
An individual Publisher can handle approximately 500 Mbps of throughput, and can handle approximately 32,000 concurrent UDP orTCP connections.
How much downtime should I expect during Publisher upgrades and/or failover to secondary Publisher?
Single Publisher: 1-3 minutes as the system is upgraded until the Publisher comes up.
HA Publishers: Less than 5 seconds as the traffic switches to the other Publishers in the app definition.
Can I re-enroll an existing Publisher?
No. Re-enrolling a Publisher is not currently supported.
Can the Publisher utilize autoscaling functionality of Public Cloud platforms?
Yes. Netskope Publishers can utilize the native autoscaling capabilities of Public Cloud platforms via Netskope REST API or automation tools such as Terraform.
Can syslog be set up on a Publisher?
Yes. The basic steps are:
SSH into the Publisher.
Select the menu option
Configure syslog
.
Provide the syslog server host/IP and port.
The Publisher restarts to apply the settings, and sends these entries to the configured syslog server.
For Private Application allowlisting, what IP Address is seen at the Private App level from NPA?
The Private Application Host will see the connection as originating from the IP address of the Publisher that is connecting to it. There is no range, but depending upon the number of Publishers used to connect to the Private Application Host, you will need to allowlist each of those IP addresses.
What access needs to be allowed for NPA to work correctly?
Component
URL
Port
Notes
Client
gateway.npa.
<tenant-domain-suffix>
Example:
gateway.npa.goskope.com, gateway.npa.eu.goskope.com, ..)
addon-
<customer-tenant-url>
Example:
addon-acme123.goskope.com
nsauth-
<customer-tenant-url>
Example:
nsauth-acme123.goskope.com
TCP 443 (HTTPS)
Requires outbound access only.
The addon URL is typically required for retrieving feature flags and IDP enrollment.
The nsauth URL is required for the Periodic Re-authentication feature.
Publisher
stitcher.npa.
<tenant-domain-suffix>
Example:
stitcher.npa.goskope.com
addon-
<customer-tenant-URL>
Example:
addon-acme123.goskope.com
dns.google
*.docker.com
*.docker.io
*.ubuntu.com
Note
If your Publisher is running in China, you need to add the following two domains into the allowlist.
ns-1-registry.cn-shenzhen.cr.aliyuncs.com
npa-ova.oss-cn-shenzhen.aliyuncs.com
TCP 443 (HTTPS)
UDP 53 (DNS)
TCP 80 (HTTP) for
*.ubuntu.com
Requires outbound access only.
The
addon
URL is typically required for retrieving feature flags.
Note
For administration, please allow
TCP 22
(SSH) from admin subnets to the Publisher.
For Publisher updates, allow outbound access to:
*.docker.com
*.docker.io
docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com
for TCP 443 outbound.
*.ubuntu.com
for TCP 80 and TCP 443 outbound.
Client and Publisher
ns
-<tenant-ID>
.
<MP-name>
.npa.
<tenant-domain-suffix>
Contact your Netskope SE, TSM, or Support for your tenantid and mp-name and if IP subnets are needed instead of FQDNs.
TCP 443 (HTTPS)
Requires outbound access during enrollment/re-enrollment of NPA for the Client and for registration of the Publisher.
Example URL:
ns-1234.us-sv5.npa.goskope.com
MP-Name Variables:
us-sv5
(SV5)
us-sjc1
(SJC1)
us-sjc2
(SJC2)
de-fr4
(FR4)
nl-am2
(AM2)
au-mel2
(MEL2)
ch-zur2
(ZUR2)
uk-lon3
(LON3)
sg-sin2
(SIN2)
de-fra2
(FRA2)
us-dfw3
(DFW3)
sa-ruh1
(RUH1)
Note
Requires allowing inbound access only if using a CRL server that is maintained internally within your infrastructure for Prelogon enrollment, or enabling Browser Access. This is not needed for the dataplane traffic.
For allowlisting
ns-
<tenant-ID>
.
<MP-name>
.npa.
<tenant-domain-suffix>
based on IP addresses, refer to the
Netskope Private Access List for Allowlisting
section
here
.
Client and Publisher
gateway.gslb.goskope.com
gateway.npa.
<tenant-domain-suffix>
TCP 443 (HTTPS)
Netskope is transitioning away from the old EDNS and LDNS mechanisms over DNS and DNS-over-HTTPS.
For most customers, the DNS rules will be used as a fallback mechanism, and this is the preferred method, meaning the primary mechanism is through an API connection over HTTPS to our GSLB gateway.
Consult with your technical contacts at Netskope to validate which rules are exactly needed.
Client and Publisher
dns.google
TCP + UDP 53 (DNS) TCP 443 (DNS-over HTTPS / DoH)
For identifying the closest Netskope Data Center, the Client leverages EDNS as the secondary method, so TCP 443 using DNS over HTTPS to dns.google needs to be allowed. (Corresponding IPs are
8.8.8.8, 8.8.4.4).
The fallback to EDNS is Local DNS (LDNS), so DNS (UDP 53) will need to be allowed to the DNS resolver.
Netskope is transitioning to our new GSLB API for identifying datacenters. Consult with your technical contacts at Netskope to validate which rules are exactly needed.
I’m not certain what TCP/UDP ports my application needs in order for it to work. What can I do?
To connect users with applications/services, an NPA administrator must configure Private App policies within the Netskope UI in a few places. Here are the configuration options and details for known application/service types.
Application
Protocol/Port
Factors
Web Traffic
TCP: 80, 443
(custom ports: 8080, etc.) UDP: 80, 443
Google Chrome will use the QUIC protocol (HTTP/S over UDP) for some web applications, so duplicating the web browsing ports for both TCP and UDP can provide a performance improvement
Secure Shell (SSH)
TCP: 22
Remote Desktop (RDP)
TCP: 3389
UDP: 3389
Some Windows RDP client apps (in particular, newer Windows 10 versions) will now prefer to use UDP:3389 to perform Remote Desktop connectivity
Windows SQL Server
TCP: 1433, 1434
UDP: 1434
The default port for Windows SQL Server is 1433, though this can be customized in your environments. Refer to the Microsoft
documentation for more details: Configure the Windows Firewall to Allow SQL Server Access.
MySQL
TCP: 3300- 3306, 33060 TCP: 33062 (for admin specific connections)
For general MySQL connection use cases, only port 3306 is required, but some customers may take advantage of the additional MySQL feature ports. Netskope recommends using a port range for MySQL database private apps. MySQL will block connections from the NPA Publisher because it detects the reachability test as a potential attack. Using a range in the port configuration will result in the NPA Publisher performing a reachability check only on the first port in the range and therefore prevent MySQL from seeing this traffic and avoiding the port block.
For further specifics, please reach out to your Netskope Technical Success Manager or Sales Engineer for assistance.
Can NPA tunnel protocols and ports outside the common ones listed above?
Yes. NPA can tunnel apps outside of that list. NPA supports both the TCP and UDP protocols and all associated ports, with one notable exception: Netskope does not currently tunnel most DNS traffic, but we do support tunneling DNS SRV lookups over port 53. This is needed for service discovery, which is used in various Windows AD scenarios involving LDAP, Kerberos, etc.
Note
Sometimes applications like VoIP can be problematic. Not so much due to tunneling, but rather configuration. For example, applications that perform dynamic port allocation when establishing a connection can be problematic, because an admin cannot know which ports will be set up by the service end of the application in advance, so there’s no way to know what ports to specify.
What protocols and ports can NPA tunnel for Private Applications?
NPA can support any client to server TCP and UDP traffic.
Can NPA tunnel ICMP?
No. NPA does not tunnel ICMP, only TCP and UDP. So you cannot
ping
or
traceroute
over NPA to test network connections. To quickly check whether NPA steering is working for a private application defined by FQDN,from a command prompt/Terminal window, enter:
nslookup
<FQDN_of_Private_App>
. You can utilize tcping, psping, or other tcp based tools to test connectivity.
Does NPA support tunneling connections established from a private app to a Client?
No. NPA does not support protocols that establish connections from a private app to a Client. For example, FTP Active mode is not supported.
What is SRP and how does NPA leverage SRP to steer traffic?
The SRP is a document describing a list of apps available to a user. When an NPA tunnel is established for a given user, the NPA management plane performs the calculation of the Service Routing Protocol (SRP). Also, SRP may be revised dynamically based on changes made to the NPA policy, steering, application, device posture or group membership changes.
Based on the SRP, NPA filters and tunnels private application traffic to the NPA dataplane, and if allowed, then forwards it through the NPA infrastructure to the private app. If not allowed, the NPA dataplane blocks the traffic.
Important
Starting in Release v118, the Netskope Private Access backend will drop traffic if the resulting SRP is greater than 40MB.
This is a protection mechanism to shield misconfigurations from one tenant from harming the overall solution.
Any large Private App policies, such as enumeration of large number of ports one-by-one, must be disabled to reduce the size and unblock access to those users.
If these configurations cannot be optimized, please reach out to Netskope Support for additional assistance.
How long does it take for a client to receive new policy changes (like having a new Private App assigned to them, and have the changes propagate to the Client)?
Currently each client checks in with the management plane every 15 mins to see if any policy changes need to be downloads and SRP needs to be recalculated. As such, it should take no longer than 15 minutes for new policy changes to propagate to all clients. In reality, it can be from a few seconds to 15 minutes based on the position of timer on the particular client.
Optionally, you can verify the most recent NPA Policy update by looking at the bottom of the
npadebuglog.log
for the string
SRP live status is 1
, and verifying the last timestamp for the log entry. You may see dozens of log entries; just make sure you look for the newest one.
How does the the Netskope Client check for configuration updates?
The Client auto-checks for updates as set by the administrator or end-user.
Does the Client send state changes for updated authentication?
Yes. The Client provides both periodic and dynamic updates, such as device classification, authentication status, and user to the controller for authorization information.
What is a good method for troubleshooting accessibility issues to a private app/service behind a Publisher?
The first best option is to use the Troubleshooter. Click
Troubleshooter
on the
Private App Segments tab in the App Definition
page.
Select a
Private App Segment
and choose an access method.
For Client, select a user, and click
Troubleshoot
.
For Browser Access, enter a custom hostname and select a user, and click
TroubleShoot
.
The Troubleshooter renders the list of executed checks, problems which may affect your configuration, and solutions for these problems.
The Troubleshooter has about a dozen of checks now. However, there are multiple additional conditions which could affect access (which Troubleshooter doesn’t check). As a result, it is useful to be able to run some of the checks manually.
In this Topic
Private Access FAQs

---
## Source IP Anchoring for an IdP with Netskope Private Access
**URL:** https://docs.netskope.com/en/source-ip-anchoring-for-an-idp-with-netskope-private-access/
**Last Modified:** 2026-01-27T00:34:15+00:00
**Scraped:** 2026-09-03T10:48:05.794853+00:00

Source IP Anchoring for an IdP with Netskope Private Access
Background
Many organizations have been utilizing IP address allowlisting on their corporate cloud apps in order to ensure additional security should a user’s credentials be compromised by a malicious actor. This allowlisting is inclusive of all egress IP addresses for your data centers and remote offices. Typically for remote users, a VPN connection is required to access private applications and also their corporate cloud applications.
With Netskope, the traffic flow changes when utilizing the Netskope Client. Because the Netskope Client encrypts its connections to the Netskope proxy, cloud applications and IdP providers no longer see the corporate egress IP addresses and instead see an IP addresses for Netskope’s POPs.
The preferred solution is to add Netskope’s POP IP addresses to your IP address allowlisting for conditional access and employ multi-factor authentication (MFA) with your IdP provider. If you do not want to use MFA or open up access to your cloud applications to Netskope’s POP IP address ranges, the following is an alternative solution to preserving your dedicated IP addresses when accessing SaaS apps or web sites.
Solution
Let’s assume you are using an IdP provider like Okta, and that you have only one data center for all of their traffic.
By default, all Okta traffic is steered to Netskope proxy. This method changes this default behavior. Instead of sending Okta traffic through the Netskope proxy, this method defines your Okta URL as a
private application
inside of Netskope Private Access.
Netskope Publisher
: There are a couple of options. You could deploy a Publisher inside your existing corporate data center. All Publisher traffic would be seen as your existing egress IP address (1.1.1.1).
Another option is to determine where your Okta instance is located, and deploy a Publisher in AWS, GCP, or Azure within a region that is closer to Okta instance.
Open up a Terminal/Command Shell and try pinging your tenant URL:
You can see in the response, this Okta tenant is located in US-West-2 Region inside of AWS. Since you’re East Coast based, it would be better to deploy a Publisher in the US-West-2 Region of AWS so the Netskope Security Cloud can provide the most optimized path to Okta from wherever the remote user is located without having to route back to the east coast data center just to go to the west coast data center for Okta.
In AWS
Go to the AWS console.
Deploy the Publisher AMI image into the West region of AWS and make note of the Public IP Address. Best practice for a production deployment of a Publisher is to use an elastic IP address so that if the Publisher is rebooted, it will keep the IP address across reboots.
Okta:
netskopepartners.okta.com
Okta Location:
AWS US-West-2 Region
Customer Corporate Egress IP:
1.1.1.1
Customer Location:
East Coast
Netskope Publisher Egress IP:
54.193.39.103 (US-West-2 Region)
In Netskope
In your Netskope tenant, go to
Settings > Security Cloud Platform > App Definition
, click on the
Private App Segments
tab, and click
New Application Segment
. Enter the parameters as shown and click
Save
.
Use this Private App Segment in a Real-time Protection policy for Private Access.
This is going to force ONLY the Okta traffic to be sent via NPA publisher. The Publisher IP address is an IP address that the customer is
renting
from AWS and is
not shared
by other customers.
Upon a successful login to the cloud application all of the cloud app traffic will be sent from the Netskope Client directly to Netskope proxy.
In Okta
In Okta Administration, make sure you are IP allowlisting ONLY your corporate data center’s egress IP address (1.1.1.1) and the NPA Publisher IP address (54.193.39.10). These are the only source IP addresses that the your Okta tenant will allow a successful login from (even if a malicious actors is on Netskope’s network has compromised credentials).
In Cloud Applications
You should still allow Netskope’s POP IP addresses along with your corporate egress IPs.
A phased approach to allowlist apps with Netskope IP ranges is outlined below.
Summary
With the above configuration, if a malicious actor somehow obtains compromised credentials and am also a user of the Netskope Security Cloud, when attempting to access one of your corporate cloud applications, authentication will be redirected to Okta, but because the auth request is NOT coming from your Publisher or corporate egress IP address, a log in attempt will fail, even with valid credentials.
Phased Approach for Allowlisting Netskope IP Ranges
This phased approach has been deployed by users that have IP allowlisted around120 SaaS applications.
Phase 1
: Bypass all of your 120 sanctioned apps in Netskope. Don’t steer the apps until you allowlisted the Netskope IP ranges in each SaaS app.  You will receive immediate visibility to ~2300 unsanctioned cloud applications, as well as all web site traffic, if you use Netskope Secure Web Gateway in place of your existing SWG.
Phase 2
: Add Netskope IP ranges to your sanctioned apps.  This doesn’t have to be all at once – you could add our ranges in batches.
Phase 3
: As you allowlist the Netskope IP ranges to your SaaS apps, add sanctioned SaaS apps back to Netskope steering config so they pass through the NewEdge network for visibility, control, DLP, threat detection, etc.  Note – we purchased a /17 network so we have plenty of room for our future POPs that we’ll be adding around the globe.  Once you add our ranges you should not have to adjust them again due to the public IP space we have.Continue until all of your 120 SaaS apps have the Netskope IP ranges added to their Allowed List.
In this Topic
Source IP Anchoring for an IdP with Netskope Private Access

---
## View Private Access Status for Devices
**URL:** https://docs.netskope.com/en/view-private-access-status-for-devices/
**Last Modified:** 2026-03-03T01:35:40+00:00
**Scraped:** 2026-09-03T10:49:29.505321+00:00

View Private Access Status for Devices - Netskope Technical Documentation
View Private Access Status for Devices
After the Netskope Client is installed and enabled on devices, you can check the status of each device.
Go to
Settings > Security Cloud Platform > Devices
.
Click the gear icon
on the far right of the table header row.
Enable the
Private Access Status
checkbox.
The status of each device is now shown on the page.
In this Topic
View Private Access Status for Devices

---
## What Do the Private Access Device Status Types Mean?
**URL:** https://docs.netskope.com/en/what-do-the-private-access-device-status-types-mean/
**Last Modified:** 2026-03-03T02:28:39+00:00
**Scraped:** 2026-09-03T10:49:53.368255+00:00

What Do the Private Access Device Status Types Mean? - Netskope Technical Documentation
What Do the Private Access Device Status Types Mean?
The Netskope Client monitors and transmits the status of the Secure Access tunnel as a status element included with each Client status event message. For NPA Client status information, go
here
. Also, the
npa_status
field on the Devices page of the Netskope tenant will contain one of the following values:
Enabled
: Represents NPA tunnel is connected.
Disabled
: Tunnel may be disabled by the user or the admin, or the tunnel is disconnected.
Errored
: NPA tunnel is disconnected due to error.
In this Topic
What Do the Private Access Device Status Types Mean?

---
## Windows Autopilot with Private Access Prelogon
**URL:** https://docs.netskope.com/en/windows-autopilot-with-private-access-prelogon/
**Last Modified:** 2026-01-16T00:46:36+00:00
**Scraped:** 2026-09-03T10:50:00.087906+00:00

Windows Autopilot with Private Access Prelogon - Netskope Technical Documentation
Windows Autopilot with Private Access Prelogon
Traditionally IT administrators spend a lot of time on building and customizing OS images, compatibility testing with various device makes and models etc. Every device typically goes through a re-imaging process with additional pre and post validation to make sure it is ready for use in the field. This process implies major cost and time effort.
Windows Autopilot is a collection of Microsoft technologies working in concert that help to simplify and streamline the bulk deployment, setup, and configuration of Windows 10/11 devices in organization to ensure they are provisioned and locked down according to corporate standards. Autopilot also can be used for device reset, repurpose and recovery.
Windows Autopilot enables customers to:
Recognize company owned devices and associate them with appropriate enrollment workflows and configuration profiles.
Automatically join devices to Entra ID.
Auto-enroll devices into MDM services such as Intune.
Customize Out of Box Experience (OOBE) content specific to the organization.
More information about Microsoft Autopilot can be found here:
https://docs.microsoft.com/en-us/mem/autopilot/windows-autopilot
.
How does Device Prelogon Access Work
A Prelogon connection operates on a machine-level context, therefore traditional interactive authentication methods won’t be available. The Netskope Client gets preconfigured and rolled out with a tenant identification token. This token helps Netskope Private Access to process incoming requests based on the policies configured in your Netskope UI. Factor that the token is shared across the entire Netskope tenant and its accidental or malicious loss may result in unauthorized access to Active Directory and/or other resources exposed for prelogon connectivity.
Netskope highly recommends enabling a safeguard mechanism against accidental token loss or disclosure. This safeguard mechanism represents an additional authentication factor which can be extracted from the machine context for validation of the machine certificate.
The Autopilot enrollment process may include an additional phase that will trigger machine certificate generation, signing by Active Directory CA, and distribution to the enrolled devices via Intune. Eventually the device that just completed the Autopilot enrollment process will have a unique machine certificate which will be mandatory for origination of prelogon tunnel.
Netskope performs cryptographic validation of the machine certificate to ensure it is not forged and is issued by the trusted internal enterprise CA (such as Active Directory Certificate Authority). The prelogon tunnel will be established only after successful validation.
Windows Autopilot Hybrid Entra ID
Many organizations heavily rely on on-premises Active Directory capabilities, such as a Group policy, authentication (Kerberos and NTLM), and file sharing services (SMB, DFS). While there is a desire to adopt modern device management framework such as Autopilot, it is important to retain an existing set of technologies and ensure its compatibility with on-premises active directory infrastructure.
There are a few different types of Windows Autopilot profiles aiming to address different deployment scenarios. This article is covering the Autopilot type
Hybrid Entra Join
. In this scenario, Autopilot adds the device to an on-premises active directory and performs device enrollment into Intune.
The above high level architecture diagram illustrates critical components required to enable Autopilot Hybrid Entra Join. More information about prerequisites and deployment steps can be found in this Microsoft article:
https://docs.microsoft.com/en-us/mem/autopilot/windows-autopilot-hybrid
Secure Connectivity to an On-premises AD via Netskope
One of the biggest benefits of Autopilot based enrollment is an accelerated timeline for the user to onboard with their IT-issued endpoint(s) in their possession. Devices can be shipped to users right from the manufacturer, bypassing centralized IT organization. A user just needs to unbox the device, connect to power and the local Wi-Fi network, enter corporate credentials, and the Autopilot process will take it from there.
The result of the Autopilot enrollment process would be a fully provisioned hardened device ready for business use. It will not have any local accounts configured; a user must use domain credentials as the only way to access a device. There are no cached credentials on the device after the enrollment is complete, therefore there must be connectivity to Active Directory at the time of initial login. For field based devices this represents an architectural challenge which Netskope Private Access (NPA) is uniquely positioned to solve.
Devices with a pre-installed Netskope Client would be enabled to access Active Directory services in a secure least privilege manner via Netskope Private Access (NPA). A Netskope client with necessary configuration parameters can be installed by Intune as a part of the Autopilot enrollment process.
After successful Autopilot enrollment, a user is presented with the standard Windows login screen. At this point user context and permissions is not yet known (because a user has not logged in yet), so Netskope Private Access establishes a Prelogon tunnel specifically designed for accessing critical infrastructure services out of the machine-level context.
After successful authentication, the Netskope Client collects the user’s identity and switches into user tunnel mode, which opens broader access to enterprise applications and services.
Configure Windows Autopilot
This document assumes your Windows Autopilot implementation is already operational. Validating correctness of device enrollment through the Autopilot process while local connectivity to Active Directory is present is recommended. Subsequent steps described in this document will enable the same Autopilot experience for the device in the field. Detailed instructions on how Autopilot should be configured are available on the Microsoft documentation portal:
https://docs.microsoft.com/en-us/mem/autopilot/windows-autopilot-hybrid
https://docs.microsoft.com/en-us/windows/deployment/windows-autopilot/demonstrate-deployment-on-vm
User Accounts Enrollment and Provisioning with Netskope
User accounts associated with Autopilot deployment should be synchronized with the Netskope UI so that user provisioning and enrollment can be enabled. More information about specific configure steps can be found in this Microsoft article:
https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/netskope-administrator-console-provisioning-tutorial
Deploy the Netskope Client via Intune
The following steps are required to include Netskope client deployment as a part of Autopilot deployment process:
Enable prelogon in the Netskope Tenant. In the Netskope UI, go to
Settings > Security Cloud Platform > Netskope Client >
Client Configurations
. Click on the appropriate Client Configuration, and enable
Prelogon for Private App Segments
. Create an arbitrary prelogon username, like
autopilot@prelogon.netskope.com
.
This prelogon username is used as a service account inside the Netskope tenant and should not be provisioned nor synchronized with Entra ID. It will be automatically added to the list of users in the Netskope UI and can be used for configuration of real-time access policies for private apps. Large scale deployment may include several Client Configurations associated with specific Groups or OU, and they will have individual prelogon usernames.
Click
Save
.
Add the Netskope Client in to Intune. Refer to the specific configuration steps described and this article
/en/microsoft-intune.html
. In order to enable Autopilot, use an additional argument with the prelogon username appended so the entire command line argument string looks like this:
host=addon-corp.goskope.com token=
<org ID>
enrollauthtoken=
<Authentication Token>
enrollencryptiontoken=
<Encryption Token>
prelogonuser=autopilot@prelogon.netskope.com /qn
Click
Next.
Make an assignment with the appropriate group to be used for Autopilot deployment. Click
Next
and then
Create
.
Netskope recommends choosing
App Type
as
Line-of-business app
while configuring MS Intune. If you want to choose another
App Type
such as
Windows app (Win32)
, refer to the Win32-specific instructions in
Intune with Win32 App
. Do not combine this with the LOB apps for
Autopilot deployments
.
Configure Netskope Private Access for Windows Autopilot
The section explains how to configure Netskope Private Access to enable Autopilot enrollment for devices in the field. Performing thorough testing for a test group of users before a full deployment is recommended.
Create Apps Definitions for Active Directory services according to this article:
/en/netskope-private-access-for-microsoft-active-directory-domain-services.html
If a Distributed File System (DFS) is expected to be used by users enrolled into Autopilot, associating DFS configuration objects with prelogon user accounts is recommended. More information about DFS configuration forNetskope Private Access can be found in the article
/en/netskope-private-access-for-smb-and-dfs-services.html
Create a Private Access Policy. In the Netskope UI, go to
Policies >  Real-time Protection> New Policy
and select
Private App Segment Access
. In the Source section, select the user you created earlier (
autopilot@prelogon.netskope.com
). For Destination, in the
Private App Segment
dropdown list, select the App Definitions created previously corresponding to Active Directory Services.
Provide a name for the policy and click
Save
. Make a decision about policy placement according to the existing hierarchy. More broad access control policies should be towards the bottom of the policy table. If you change the order of the policies, click
Save
again.
Click
Apply Changes
.
After completion of the above steps, full enrollment for devices in the field should be operational.
Security Considerations for Prelogon Connectivity
Autopilot deployment implies supporting connectivity to Active Directory services at the time when user context is not yet known. The above configuration relies on access control based on prelogon username and org-id token. If those values get compromised, malicious actors could use them to gain unrestricted access to Active Directory services. The Netskope Client can be downloaded on the internet and installed with the above installation parameters, which would pave a way for potential attackers to enumerate Active Directory configuration objects, attempt to exploit known vulnerabilities, perform password brute force attacks, and many other undesired activities. Remediation of such an attack could be challenging as changing a prelogon username would not be considered as a strong measure.
Based on this factor, Netskope considers a pair of prelogon username and org-id token as just identification parameters. Netskope Private Access supports strong authentication for prelogon and Autopilot use cases that can be implemented based on cryptographic validation of unique device machine certificates.
For secure generation and distribution of machine certificates please refer to your Microsoft documentation for SCEP deployments.
Netskope Private Access Enforcement-based Machine Certificates
After configuration for machine certificate generation, signing and distribution within Intune and Autopilot is complete, you need to modify Netskope Private Access configuration in order to perform validation and enforcement.
In the Netskope UI, go to
Settings > Security Cloud Platform > Netskope Client > Devices
and click
Client Configurations
. Click on the appropriate Client Configuration, and in the
Device Certificate Authority
section, upload the CA certificate. When finished, click
Save
.
The above configuration instructs the Netskope Client, as well as the Netskope Management Plane (MP), to perform cryptographic validation of the machine certificate associated with the device enrolled through Autopilot. The Netskope client performs analysis of machine certificate properties, validity period, revocation status (if enabled in Netskope console and exposed for the Netskope MP to access).
Additionally, Netskope client encrypts an arbitrary dataset with the use of the private key stored on the device, and will forward it to the MP along with non-encrypted hashed dataset. The Netskope MP performs dataset decryption with the public key and compares the resulting values. If the two values match, the result is successful cryptographic validation.
In this Topic
Windows Autopilot with Private Access Prelogon

---
## ZTNA Policy Best Practices for Session 0 (VDI Tunnel User)
**URL:** https://docs.netskope.com/en/ztna-policy-best-practices-for-session-0-vdi-tunnel-user/
**Last Modified:** 2025-08-31T01:45:44+00:00
**Scraped:** 2026-09-03T11:08:49.489119+00:00

ZTNA Policy Best Practices for Session 0 (VDI Tunnel User) - Netskope Technical Documentation
ZTNA Policy Best Practices for Session 0 (VDI Tunnel User)
Understanding Session 0:
In Windows, Session ID 0 is reserved for system services and processes running under the SYSTEM account​. Any network traffic originating from these services (e.g. Windows system services, antivirus agents) appears as “Session 0” traffic. In Virtual Desktop (VDI) or multi-user environments, this traffic is
shared by all users
on the machine and isn’t tied to any interactive user session​ (
Learn more
). This poses unique challenges for ZTNA, which often enforces policy per user.
Best Practices (Applicable to any ZTNA, including Netskope NPA):
Separate System Traffic from User Traffic:
Use ZTNA features to route system-initiated (Session 0) traffic through a dedicated channel or virtual user account. For example, Netskope NPA introduces a special “VDI tunnel user” to handle Session 0 traffic​ (
Learn more
). This ensures traffic from system processes (like SMB file share access or domain controller lookups) is identified separately and gets its own Zero Trust policies​ (
Learn more
). Generally, isolate and tag Session 0 traffic so it can be governed independently of any logged-in user.
Least Privilege Policy for Session 0:
Apply strict ZTNA policies that
only allow required system-level communications
and block everything else. Identify essential services (see table below) and explicitly permit their traffic (by destination, port, and protocol) for Session 0. For instance, allow the system to reach corporate DNS on port 53, domain controllers on Kerberos/LDAP ports, or Windows Update servers on HTTPS, but
block unauthorized or unexpected destinations
. This limits abuse. Since malware often runs as a service to get SYSTEM privileges, a least-privilege approach ensures a malicious service can’t freely communicate to internal resources or the internet.
Group Similar Users/Systems:
In VDI or multi-user scenarios, group users with similar access needs on the same host or pool​ (
Learn more
). Because Session 0 traffic is shared, having users with vastly different access requirements on one machine could cause conflicts. For example, an admin’s system processes might legitimately access more internal services than a regular user’s.
Rationale
: Grouping by access profile prevents a less-privileged user from indirectly piggybacking on system traffic needed by a high-privilege user (
Learn more
).
Implementation
: Consider separate VMs or desktops for admins vs. standard users to align Session 0 traffic policies with the users’ roles​ (
Learn more
).
Use a Consistent Dedicated Account for Session 0 Tunnel:
If your ZTNA uses a service account or virtual user for system traffic (like NPA’s VDI user), assign one consistently per host group (
Learn more
). Avoid configurations with multiple different
tunnel users
on the same machine, as this can cause tunnel instability or policy confusion​ (
Learn more
). Consistency ensures the system traffic always uses the expected identity and policy set.
Monitor and Audit System Traffic:
Enable logging and regular monitoring of Session 0 traffic through your ZTNA platform​ (
Learn more
). Audit which system processes are generating traffic and where it’s going. This helps catch misrouted traffic or potential breaches. For example, if you see the system (Session 0) trying to contact an unknown IP on an unusual port, investigate; it could be a rogue service. Netskope recommends checking client logs (like
npadebug.log
) to verify the dedicated tunnel is working and carrying only intended traffic​ (
Learn more
). Regular reviews can identify policy mismatches or needed adjustments​ (
Learn more
).
Plan for Maintenance and Updates:
Ensure your ZTNA solution is up-to-date to support these features. For NPA specifically, note that upgrading an existing client won’t retroactively enable VDI mode; a fresh install is needed​ (
Learn more
). Also be mindful that a Session 0 tunnel persists as long as any user is logged on, and only terminates when the last user logs off​ (
Learn more
). Design your policies knowing this tunnel may stay up between user sessions (like during fast user switching or brief logoff periods). Always test policy changes in a controlled way to ensure critical system functions (time sync, updates, etc.) aren’t inadvertently blocked.
By following these best practices, you ensure system-originated traffic is tightly controlled yet allowed where necessary, maintaining security without breaking essential services. The table below identifies common services/applications that run in Session 0 and the typical network traffic they generate. These should be accounted for in your ZTNA policy design.
Common Session ID 0 Network Traffic on Windows 10/11
The following table lists default Windows services and common third-party applications that frequently generate network traffic from Session ID 0 (the system context). For each, here are the ports and protocols used, and why the traffic originates from Session 0. This information is crucial for crafting ZTNA rules. You’ll want to permit legitimate traffic for these services while blocking or scrutinizing others.
Service / Application
TCP/UDP Ports
Protocol
Description (Function & Why Session 0)
Windows Time
(W32Time)
UDP/123
NTP (Network Time Protocol)
The system clock syncs with time sources as a Windows service running in Session 0. In domain-joined environments, this synchronization happens with internal domain controllers. In standalone setups, organizations often configure internal NTP servers to maintain consistent time. Time sync uses NTP/SNTP over UDP port 123. ZTNA policies should allow this traffic only to approved internal NTP servers to ensure clock accuracy, which is critical for log integrity and Kerberos authentication.
Windows Update and BITS
(Windows)
TCP/80, TCP/443
HTTP and HTTPS
The Windows Update and Background Intelligent Transfer Service (BITS) runs as SYSTEM in Session 0 to keep devices up-to-date. In enterprise environments, updates are typically sourced from an internal WSUS or SCCM server instead of the public Microsoft update servers. ZTNA policies should allow these services to reach only the organization’s internal update servers (like WSUS) over HTTP/HTTPS (ports 80/443). Blocking this access can prevent critical OS and application updates from being installed.
Active Directory Domain Services
(Kerberos, LDAP, SMB)
UDP/88, TCP/88 (Kerberos KDC)
TCP/445 (SMB/CIFS)
TCP/389 (LDAP; 636 for LDAPS)
Kerberos, SMB, LDAP
When a device is joined to an Active Directory domain, it communicates with internal domain controllers in Session 0 using the SYSTEM context. This includes Kerberos (TCP/UDP 88), LDAP/LDAPS (TCP 389/636), and SMB (TCP 445) for authentication, directory access, and Group Policy processing. ZTNA should allow these protocols only to designated internal domain controllers. Preventing access would disrupt domain logins and policy enforcement, while overly broad access increases risk of lateral movement.
Certificate Revocation and OSCP Checks
(Windows)
TCP/80 (HTTP)
TCP/443 (HTTPS)
HTTP (CRL/OCSP)
Windows services running in Session 0 periodically validate certificates using CRLs and OCSP, typically over HTTP/HTTPS. In enterprise setups with internal PKI or SSL inspection, these checks are directed to internal certificate validation infrastructure or approved proxy services. ZTNA policies should allow CRL/OCSP traffic only to internal or explicitly trusted certificate servers to ensure secure TLS communications and prevent certificate-related failures.
Symantec Endpoint Protection (SEP)
(Enterprise AV)
TCP/8014 or 80 (HTTP)
TCP/443 (HTTPS)
HTTP/HTTPS (REST API)
Symantec’s endpoint agent (SEP) runs as a SYSTEM service in Session 0, communicating with an internal Symantec Endpoint Protection Manager (SEPM) for policy and definition updates. This uses HTTP port 8014 (or optionally HTTPS 443). ZTNA should allow this traffic only to the internal SEPM server. Blocking it will prevent the endpoint from receiving security updates and could impact threat detection.
McAfee ePO Agent
(Endpoint Mgmt)
TCP/80 (HTTP)
TCP/443 (HTTPS)
HTTP/HTTPS
The Trellix (formerly McAfee) Agent operates in Session 0 to connect with the internal ePolicy Orchestrator (ePO) server for policy sync and reporting. Modern agents use HTTPS (TCP 443), while older ones may use HTTP (port 80). ZTNA policies should permit this traffic only to the internal ePO server. Inbound management (like wake-up calls on port 8081) typically happens within the LAN and doesn’t need remote ZTNA allowance.
SCCM/ConfigMgr Client
(Microsoft Endpoint Configuration Manager)
TCP/80 (HTTP)
TCP/443 (HTTPS)
(TCP/445 SMB for some content)
HTTP/HTTPS, SMB
The SCCM client runs as a SYSTEM service and communicates with internal management and distribution points for software deployment and compliance. This typically uses HTTP or HTTPS (ports 80/443), and sometimes SMB (TCP 445) for content delivery. ZTNA rules should allow outbound traffic only to internal SCCM infrastructure (management points and content distribution points). Without this, endpoints may fail to receive applications, updates, or configuration baselines.
Note that the above list is not exhaustive, but covers the most common system-originated network traffic on Windows clients. Other services or third-party agents (backup software, monitoring agents, print spooler to network printers, etc.) may also send Session 0 traffic. Always review what’s installed on your hosts and adjust policies accordingly.
Security Considerations and Mitigations for Session 0 Traffic
Properly handling Session 0 traffic in ZTNA is crucial for security and functionality. Misconfiguring it can either break core services or introduce security gaps. Here are some key considerations:
Ensure Essential Services Are Allowed:
From the table, identify which services are in use in your environment and verify your ZTNA policy permits their required traffic. For example, if the device is domain-joined, allow it to reach domain controllers on Kerberos, LDAP, or SMB. If you use a particular EDR or AV agent, allow its cloud communication. Blocking these can lead to system malfunctions (like failing to apply Group Policy if Kerberos or SMB is blocked​ (
Learn more
). Always restrict the allowed destinations to the minimum (like only your organization’s AD servers, and only the vendor’s cloud addresses for EDR) to reduce risk.
Restrict and Inspect Non-Essential Traffic:
Any network traffic from Session 0 that is not explicitly needed should be blocked by default. Since services run with high privileges, malware or attackers often abuse them to spread or exfiltrate data. For instance, an attacker who gains SYSTEM access could try to use the machine’s network access to scan or connect to internal systems. A Zero Trust policy should prevent the SYSTEM context from reaching anything not on the approved list (principle of least privilege). Consider enabling logging or alerts for unusual Session 0 connections, like the system process attempting to contact an IP or port that doesn’t match any known service. This could indicate malicious activity leveraging a service process.
Separate Policy Rules for Session 0 (VDI Tunnel User):
It’s a best practice to manage Session 0 traffic under a distinct policy identity (like the dedicated VDI user in Netskope NPA​,
Learn more
). This way, you can craft tighter rules without affecting user-initiated traffic. For example, a regular user might be allowed to access many internal web apps, but the system (Session 0) really shouldn’t be initiating connections to those in most cases. By segmenting policies, you can
enforce stricter controls on system traffic
, like only allow DNS to your DNS server, Windows updates to Microsoft, and block everything else. This segmentation contains any potential misuse of system processes.
Mitigate Lateral Movement and Spoofing:
Be cautious with services like SMB (445) that could be used for lateral movement. Ideally, the ZTNA broker should only allow the endpoint’s Session 0 SMB traffic to specific servers (file servers or domain controllers) and drop attempts to reach other clients. Similarly, limit RPC or other internal service ports. This prevents a compromised host from acting as a pivot using its SYSTEM-level network access. If possible, enable client device authentication for system-initiated traffic as well (some ZTNA solutions can use device identity or posture checks in addition to the
tunnel user
identity).
Monitor Compliance and Adjust:
Continually monitor Session 0 traffic patterns. If you deploy a new software agent (like a new backup solution) that uses a system service, update your policies to allow its necessary traffic. Conversely, if you find allowed system traffic that is no longer needed (perhaps a legacy service that was removed), tighten the policy. Regular audits help maintain a strong security posture.
By following these practices: allowing what’s needed, denying everything else, and isolating/monitoring Session 0 traffic, you can safely enable critical Windows services and third-party agents through ZTNA. This approach minimizes the attack surface while ensuring that essential system functions (updates, time sync, domain connectivity, security agents, etc.) work reliably under a Zero Trust model. Each organization should tailor the specifics to their environment, but the general theme is
strict control and visibility
over all system-originating traffic.
Sources:
Windows OS network behavior and port requirements​ (
Learn more
);
Netskope NPA VDI configuration guide​
; Microsoft and vendor documentation for services and applications as cited in the table above.
In this Topic
ZTNA Policy Best Practices for Session 0 (VDI Tunnel User)

---
## Configuring Enterprise Browser and Private Access Integration
**URL:** https://docs.netskope.com/en/configuring-enterprise-browser-and-private-access-integration/
**Last Modified:** 2026-03-17T17:02:33+00:00
**Scraped:** 2026-09-03T11:18:01.591813+00:00

Configuring Enterprise Browser and Private Access Integration - Netskope Technical Documentation
Configuring Enterprise Browser and Private Access Integration
Enterprise Browser for Private Apps provides secure, seamless access to SaaS and private applications on managed and unmanaged devices without compromising data protection. Built on Chromium with a self‑service install, it’s ideal for BYOD, contractors, and fast onboarding (e.g., M&A). It enforces browser‑level controls (like copy/paste, print, etc.) and simplifies private app access by avoiding complex DNS configurations or URL rewrites, creating a secure, efficient workspace for IT and end users.
How private app definitions work when Enterprise Browser is enabled
For customers with both Enterprise Browser and Netskope Private Access (NPA) entitlements, Browser Access apps fall into two categories:
Two types of NPA browser applications
“Any Browser” applications
These are the traditional
reverse-proxy, browser-based access
apps (Browser Access) and continue to operate the same way when Enterprise Browser is enabled.
Can be accessed from
any standard browser
.
Always have a
Public Host
(and optionally a Custom Host).
Users reach them via the portal or by directly typing the Public/Custom Host, e.g.
https://ns-xxxx-443-tenant.region.npaproxy.goskope.com
In policy, these are evaluated only when the
Access Method is “Browser Access”
.
Enterprise Browser can also use them, but when it does so via the Public Host, it is still treated as
Browser Access
, not “Enterprise Browser” access.
“Enterprise Browser” applications
These are designed specifically for use with Enterprise Browser.
No Public Host
is defined.
Defined only by
internal host/IP and port
(for example: 172.31.46.99:8080 or app.internal.corp:443).
Users access them via the portal or by typing the
internal URL or IP
directly in Enterprise Browser.
Traffic is steered by Enterprise Browser to the
NPA explicit proxy (“ebnpa” proxy) on port 8090
.
In policy, these are evaluated only when the
Access Method is “Enterprise Browser”
.
Key enhancement:
Enterprise Browser applications support:
IP subnets
(e.g. 10.0.0.0/24)
Wildcard hostnames
(e.g. *.corp.local)
This is not supported for “Any Browser” apps, making Enterprise Browser apps more flexible for large / dynamic internal environments.
Conceptual takeaway for customers:
“Any Browser” apps =
reverse-proxy browser-based access
model with a public entry point, usable from any standard browser.
“Enterprise Browser” apps = private/internal entry point, Enterprise Browser only, with subnet/wildcard support.
What changes in policy behavior
When creating an NPA policy, customers choose an
Access Method
and then attach browser apps:
Browser Access access method
Evaluates only
“Any Browser”
applications.
Enterprise Browser access method
Evaluates
both
:
“Any Browser” applications for backward compatibility, and
“Enterprise Browser” applications.
Gives Enterprise Browser users a unified experience for all browser‑based private apps.
Client access method
Evaluates only
Client
applications (unchanged behavior).
High‑level workflow
Prerequisites
Before you start, make sure the following are in place:
Enterprise Browser is deployed
Enterprise Browser is installed for target users and linked to the correct Netskope tenant.
Enterprise Browser is configured with the Netskope explicit proxy / PAC so web traffic is steered through Netskope.
NPA Private app segments and Publishers are configured for access via Enterprise Browser
NPA Publishers are deployed, healthy, and can reach the internal apps.
Required private app segments are configured so Publishers know how to reach the appropriate application networks.
Identity and access are ready
SAML and IDP
integration with Netskope is configured and tested.
The users / groups who will use Enterprise Browser + NPA are synchronized to Netskope and available for policy.
Network connectivity requirements
Enterprise Browser proxy bypass is configured so Enterprise Browser can reach required auth and control‑plane endpoints (for example, authservice.goskope.com, IdP URLs) without being accidentally bypassed.
Configure NPA policies and Enterprise Browser browser‑control policy
Configure or update policies as follows:
NPA policies
Use
Access Method = Enterprise Browser
.
Allow the NPA Browser Applications you defined in the previous step.
Best practice: keep
separate policies
for:
Browser Access
(for “Any Browser” reverse‑proxy browser‑based apps), and
Enterprise Browser
(for Enterprise Browser apps).
Enterprise Browser browser‑control policies for private apps
Create or update Enterprise Browser browser‑control policies for Enterprise Browser private apps.
Publish configuration and update Enterprise Browser
Save and publish the relevant NPA applications and policy changes.
Enterprise Browser will download an updated
PAC file
that:
Lists all internal hosts / ports from your NPA Browser Applications (npaList).
Steers matching destinations to the
NPA Proxy
(<tenant>.ebnpa.goskope.com:8090).
Access private apps using Enterprise Browser
Once policies and the PAC file are updated:
Users open the app in Enterprise Browser using the
internal host / IP:port
configured on the NPA Browser Application (there is no Public Host).
How private apps are accessed via Enterprise Browser
When users access private applications with Netskope Enterprise Browser, they connect using the internal host or IP defined on the NPA Browser Application (for example, https://172.31.46.99:22 or https://app.internal.local:443).
Enterprise Browser uses an explicit proxy PAC configuration that classifies these destinations as NPA traffic and forwards them to the dedicated NPA Proxy (
<tenant>
.ebnpa.goskope.com:8090). The NPA Proxy terminates TLS from Enterprise Browser, authorizes the user and application, and then builds the internal HTTP/HTTPS or TCP connection toward the private app via the Publisher.
You can verify this behavior from Enterprise Browser by navigating to netskope://policy and expanding
ProxySettings
. The
ProxyPacUrl
section contains a PAC file where the npaList array includes all internal hosts/ports for NPA Browser Applications. Any URL whose host:port matches an entry in npaList is steered to the NPA Proxy; everything else goes to the Enterprise Browser Edge Proxy (eproxy-
<tenant>
.goskope.com:8090) or is sent direct if it matches the bypassList.
Feature parity with reverse‑proxy browser‑based access
Enterprise Browser for private apps extends the same key capabilities available with reverse proxy, browser based private apps, including the
User Portal
,
Browser based AnyApp (RDP/SSH)
, and
Data Loss Prevention (DLP)
controls for web traffic to private applications. In addition, Enterprise Browser adds broader matching and application handling, including: support for IP subnets (e.g. 10.0.0.0/24), wildcard hostnames (e.g. *.corp.local), support for mixed content and embedded resources, and robust handling of complex applications that rely on multiple chained URL redirects and cross‑host navigations.
For configuration guidance and the full list of supported capabilities, including how Enterprise Browser extends support for existing reverse proxy features, see
Configure Browser Access for Private Apps
.
When to use Enterprise Browser + NPA
Use
Enterprise Browser + NPA
when you want:
“Inside-the-network” app behavior from the browser
Users access private apps using internal hostnames/IPs.
Internal redirects and hard‑coded internal links keep working without exposing “public vs. private” URLs to users.
Simpler handling of complex internal environments
You need to cover ranges of internal servers (e.g. RDP farms, multiple admin consoles).
Apps use many internal hostnames under the same domain and you don’t want to manage them one by one.
Stronger, layered security for private web apps
You prefer a managed enterprise browser with fine‑grained controls (e.g. user actions in the browser).
You want per‑app Zero Trust access to private apps without installing a full client on the endpoint.
Continue using
“Any Browser” / Reverse-proxy Browser Access
when:
You must support
any standard browser
for partners, contractors, or unmanaged/BYOD devices that can’t run Enterprise Browser.
You want a
simple web portal
with tiles that resolve to public entry points and your apps already work well that way.
In this Topic
Configuring Enterprise Browser and Private Access Integration

---
## Citrix VDI Considerations for Netskope Private Access (NPA)
**URL:** https://docs.netskope.com/en/citrix-vdi-considerations-for-netskope-private-access-npa/
**Last Modified:** 2026-04-15T01:28:32+00:00
**Scraped:** 2026-09-03T11:19:05.983583+00:00

Citrix VDI Considerations for Netskope Private Access (NPA) - Netskope Technical Documentation
Citrix VDI Considerations for Netskope Private Access (NPA)
This document supplements the existing NPA VDI documentation with Citrix-specific guidance for multi-user (multi-session) environments such as Citrix Virtual Apps and Desktops on Windows Server 2019/2022. It does not apply to single-user VDI desktops where SYSTEM process separation between users is not a concern.
Background: The Session ID 0 Assumption
The current NPA VDI architecture routes traffic from processes running under the SYSTEM account in
Windows Session ID 0
through a dedicated VDI tunnel user. This design is based on the standard Windows behavior where:
Session 0 is reserved for system services and non-interactive processes running as
NT AUTHORITY\SYSTEM
.
User sessions (Session 1, 2, 3, etc.) contain interactive user applications.
Network traffic originating from Session 0 cannot be attributed to any specific logged-in user and is therefore handled by the dedicated VDI tunnel.
This model works well for platforms like Azure Virtual Desktop and Amazon AppStream, where SYSTEM-level services generally conform to the standard Windows Session 0 isolation model.
The Citrix Exception: SYSTEM Processes in User Sessions
Citrix Virtual Apps and Desktops (VDA) deviates from this model. The Citrix VDA architecture spawns several processes that run under the SYSTEM account (
NT AUTHORITY\SYSTEM
), but operate inside user sessions (Session 1, 2, etc.) rather than Session 0. This is by design. Citrix’s ICA/HDX protocol requires session-aware service processes to manage virtual channels, printing, audio redirection, and session lifecycle within each user’s context.
Why Citrix Does This
Citrix’s virtual channel architecture uses a shell process and various service hosts that must run within the user’s terminal services session to properly manage per-session resources. As described in Citrix’s ICA virtual channel documentation:
The Shell (
WfShell.exe
on server OS,
PicaShell.exe
on workstation OS) loads virtual channels within the user session.
Some virtual channels are hosted as Windows services that provide one-to-many semantics for multiple applications in a session and multiple sessions on the server.
Session management processes need to run in the user’s session context to manage drive mappings, printers, clipboard, audio, and other HDX features.
Impact on the NPA VDI Tunnel
Because these Citrix SYSTEM processes run in user sessions (not Session 0), the NPA client’s session-based traffic attribution encounters the following issues:
Traffic not captured by VDI tunnel
: SYSTEM traffic originating from non-Session-0 is not routed through the dedicated VDI tunnel user, since the VDI tunnel only handles Session 0 traffic.
Potential misattribution
: The NPA Client may attempt to attribute this SYSTEM traffic to the user session it resides in, but because the process runs as SYSTEM (not as the logged-in user), policy matching may fail or produce unexpected results.
Traffic drops or connectivity failures
: If the SYSTEM-originated traffic from a user session doesn’t match either the VDI tunnel user policy or the interactive user’s policy, it may be dropped, causing failures in SMB file access, printing, DNS resolution, or other Citrix-dependent services.
Known Citrix SYSTEM Processes in User Sessions
The following Citrix VDA processes are known to run as
NT AUTHORITY\SYSTEM
inside user sessions (non-Session-0). This list is based on Citrix Virtual Apps and Desktops 7 2203 LTSR and 2402 LTSR, but applies broadly to modern VDA versions.
Confirmed: SYSTEM Processes in User Sessions
The following process is confirmed to run as
NT AUTHORITY\SYSTEM
inside user sessions (spawned as a child of
winlogon.exe
within the user’s session):
Process
Path
Function
Network Traffic
PicaSessionAgent.exe
C:\Program Files\Citrix\HDX\bin\
PortICA/HDX Session Agent: Manages per-session HDX settings, session lock/unlock, disconnect handling.
Minimal direct network traffic, but coordinates session lifecycle
Likely: SYSTEM Processes Operating in User Session Context
The following processes are part of Citrix’s ICA/HDX session architecture and are known to operate within user session context. They should be verified in your specific environment using the procedures in
Identifying SYSTEM Processes in User Sessions
, as their exact session ID behavior may vary by VDA version and configuration.
Process
Path
Function
Network Traffic
wfshell.exe
C:\Program Files\Citrix\System32\
WinFrame Shell / Seamless Engine: Manages user session environment: drive mappings, virtual channels, printers, published app windows.
SMB (TCP/445), potentially DNS
picaSvc.exe
/
picaSvc2.exe
C:\Program Files\Citrix\ICAService\
Citrix ICA Service: Core session connectivity and virtual channel hosting.
ICA protocol traffic, internal communication
CpSvc.exe
C:\Program Files\Citrix\System32\
Citrix Print Manager Service: Creates/manages network printer connections during ICA session logon/logoff.
Print spooler traffic (TCP/9100, SMB/445 to print servers)
PicaVcHost.exe
C:\Program Files\Citrix\ICAService\
Virtual Channel host: hosts virtual channels within user sessions.
Varies by virtual channel (clipboard, USB, multimedia)
HDX Supplementary Processes
Process
Function
Network Traffic
ctxaudio.exe
/ audio service
HDX audio redirection
Audio streaming traffic
CDViewer.exe
(indirect)
Session window management
Minimal network traffic
Additional Third-Party Processes
In Citrix environments, additional third-party agents may also run as SYSTEM in user sessions (not Session 0):
FSLogix Profile Agent
(
frxsvc.exe
): Profile container management, generates SMB traffic to file shares
Citrix Profile Management
(
UserProfileManager.exe
): Profile sync, generates SMB traffic
App-V client processes
(
AppVStreamingUX.exe
,
AppVShNotify.exe
): Application virtualization, started by VDA in user session context
Note that this list is not exhaustive. The specific processes present depend on the VDA version, installed features, and third-party software. See Section 5 for instructions on identifying processes in your environment.
Configuration Guidance
Since Netskope NPA’s VDI mode currently attributes SYSTEM traffic only from Session 0 to the VDI tunnel user, Citrix environments require additional configuration to handle SYSTEM traffic originating from user sessions.
Approach A: Destination-Based Steering Exceptions (Recommended)
Since NPA cannot filter by process, the workaround is to identify the destination hosts/IPs that Citrix SYSTEM processes in user sessions need to reach and create steering exceptions for those destinations. This allows the traffic to flow directly without being intercepted by NPA.
Step 1: Identify Citrix Infrastructure Destinations
Use the process identification methods in
Identifying SYSTEM Processes in User Sessions
combined with network monitoring (e.g., Wireshark, netstat, or Netskope client logs) to determine which destinations the Citrix SYSTEM processes in user sessions are connecting to. Common destinations include:
Traffic Type
Typical Destinations
Protocol / Port
SMB (file shares, home drives, profiles)
File servers, DFS namespace servers
TCP/445
Printing
Print servers
TCP/445, TCP/9100, TCP/631
DNS resolution
Internal DNS servers
UDP/53, TCP/53
Active Directory
Domain controllers
TCP/88, TCP/389, TCP/636, TCP/445
Citrix Delivery Controller communication
DDC servers
TCP/80, TCP/443
Profile management (FSLogix / Citrix PM)
Profile share servers
TCP/445
SCCM / WSUS
Management servers
TCP/80, TCP/443
Step 2: Create Steering Exceptions by Hostname
For each identified destination, create the required Destination profiles to add to a Service & Destination Profile Steering Exception.
Example hostname exceptions for a typical Citrix environment:
fileserver01.corp.example.com    # SMB file shares / home drives
fileserver02.corp.example.com    # SMB file shares / home drives
profilestore.corp.example.com    # FSLogix / Citrix Profile Management
dc01.corp.example.com            # Domain controller
dc02.corp.example.com            # Domain controller
printserver01.corp.example.com   # Print server
sccm.corp.example.com            # SCCM distribution point
Step 3 (alternative): Create Steering Exceptions by IP + Port
If you prefer more granular control, use IP + Port exceptions instead of hostname:
10.1.1.10:445      # fileserver01 - SMB
10.1.1.11:445      # fileserver02 - SMB
10.1.1.20:445      # profilestore - SMB
10.1.2.1:88        # dc01 - Kerberos
10.1.2.1:389       # dc01 - LDAP
10.1.2.1:445       # dc01 - SMB
10.2.2:88          # dc02 - Kerberos
10.1.2.2:389       # dc02 - LDAP
10.1.2.2:445       # dc02 - SMB
10.1.3.5:9100      # printserver01 - direct printing
10.1.3.5:445       # printserver01 - SMB printing
Tradeoff
: IP + Port gives tighter control but requires more maintenance (IP changes break it). Hostname is easier to maintain but bypasses all ports to that host, IP + Port is only supported when Use Publisher DNS is used.
Approach B: Expanded NPA Policy for VDI Tunnel User
For standard Windows SYSTEM services that correctly run in Session 0, maintain ZTNA policy enforcement via the VDI tunnel user:
Go to
Policies > Real-Time Protection
and edit your VDI tunnel user policy.
In the Destination field, add all private applications that Session 0 services need to access:
Domain controllers (Kerberos/LDAP/SMB)
DNS servers
NTP servers
WSUS / SCCM servers
Certificate / OCSP servers
Set the Action to
Allow
.
Limitation
: This approach only covers SYSTEM traffic in Session 0. For Citrix SYSTEM processes running in user sessions, this policy will
not
match because those processes are not in Session 0. Therefore, Approach A (destination-based steering exceptions) is still required for the non-Session-0 Citrix processes.
Approach C: Combined (Recommended for Production)
For production Citrix multi-user deployments, combine both approaches:
Destination-based steering exceptions
(Approach A) for destinations that Citrix SYSTEM processes in user sessions need to reach. This handles the non-Session-0 traffic by bypassing it from NPA entirely.
VDI tunnel user policy
(Approach B) for standard Windows SYSTEM services that correctly run in Session 0. This maintains ZTNA policy enforcement for standard system traffic.
This gives you the best balance of security and compatibility:
Standard Windows SYSTEM services in Session 0 are still governed by ZTNA policy via the VDI tunnel.
Destinations required by Citrix session infrastructure are bypassed to prevent connectivity issues caused by non-Session-0 SYSTEM traffic.
User-initiated application traffic remains fully governed by per-user NPA policies.
Security Impact of Destination-Based Bypass
Because NPA only bypasses based on destination, the steering exceptions created in Approach A apply to
all traffic
to those destinations, not just SYSTEM process traffic. This means:
User-initiated SMB traffic to the same file servers will also bypass NPA steering.
User-initiated print traffic to the same print servers will also bypass NPA steering.
Any traffic from any session to the excepted destinations goes direct.
Mitigations:
Limit exception scope
: Only add the specific hostnames/IPs that Citrix SYSTEM processes require. Do not use wildcards or broad subnet exceptions.
Network segmentation
: Rely on network-level controls (firewalls, VLANs, microsegmentation) to restrict access to excepted destinations.
Monitoring
: Log and monitor traffic to excepted destinations for anomalous patterns.
Identifying SYSTEM Processes in User Sessions
To identify which processes in your specific Citrix environment run as SYSTEM in non-Session-0 user sessions, follow this procedure:
Using a Process Explorer (Sysinternals)
Download and run Process Explorer (from Microsoft Sysinternals) on the Citrix VDA server with administrative privileges.
From the menu, select
View > Select Columns
.
In the
Process Image
tab, enable:
User Name
: Shows the account context (like
NT AUTHORITY\SYSTEM
,
DOMAIN\user
).
Session ID
: Shows which Windows session the process runs in.
Have one or more users log into Citrix sessions.
Sort by
User Name
and look for processes where:
User Name
=
NT AUTHORITY\SYSTEM
(or
SYSTEM
)
Session ID
≠ 0 (i.e., Session 1, 2, 3, etc.)
Document these processes. They are the ones affected by the Session 0 limitation.
Using a PowerShell
Run the following PowerShell command on the Citrix VDA server while users are logged in:
Get-Process | Where-Object {
    $owner = (Get-WmiObject Win32_Process -Filter "ProcessId=$($_.Id)").GetOwner()    $sessionId = $_.SessionId
    ($owner.User -eq "SYSTEM") -and ($sessionId -ne 0)} | Select-Object ProcessName, Id, SessionId | Sort-Object SessionId, ProcessName | Format-Table -AutoSize
Alternatively, using
tasklist
from an elevated command prompt:
tasklist /V /FI "USERNAME eq NT AUTHORITY\SYSTEM" /FO TABLE | findstr /V "Session:0"
Tip
: Run these commands during peak usage when multiple users are active to capture the full set of SYSTEM processes that Citrix spawns in user sessions.
Using Netskope Client Logs
Review the npadebug.log file on the VDA server to identify traffic that is being dropped or not matching expected policies. Look for:
Traffic from SYSTEM processes that is not being attributed to the VDI tunnel user.
Connection failures for services that should be accessible (SMB, printing, DNS).
Policy mismatch warnings for traffic originating from user session IDs.
Known Issues and Considerations
Steering Configuration in Multi-User Environments
Steering configuration in multi-user VDI has the following behavior:
When the first user logs in, their steering configuration is applied.
Subsequent users from different steering groups will receive the first user’s steering configuration.
To maintain consistent behavior, all users on a multi-user VDI host should share the same steering configuration.
This is particularly important for Citrix environments because the destination-based steering exceptions for Citrix infrastructure servers must be present in whichever steering configuration is active on the host.
Considerations
VDI mode requires fresh install
: Upgrading an existing Netskope Client will not enable VDI mode. A clean uninstall and reinstall with
npavdimode=on
is required.
SRPv2 not supported
: Service Routing Protocol v2 is not supported in VDI mode (support planned).
Single VDI user per host group
: Multiple different VDI tunnel users on the same machine are not supported and can cause tunnel instability.
Steering config is shared
: All users on a multi-session host share the same steering configuration (first-login wins), so destination-based steering exceptions must be consistently defined across all configurations.
Recommended Architecture for Citrix Multi-User VDI
Deployment Checklist
Install Netskope Client with
npavdimode=on
on all Citrix VDA servers.
Create a dedicated VDI user (
<username>@
vdi.netskope.com
) in the Netskope tenant.
Configure the VDI user in the Client Configuration with VDI Support enabled.
Create NPA policies for the VDI tunnel user covering standard Session 0 services (DNS, AD, NTP, Windows Update).
Identify Citrix SYSTEM processes in user sessions
using Process Explorer / PowerShell (see
Identifying SYSTEM Processes in User Sessions
).
Map the network destinations
those SYSTEM processes connect to (file servers, print servers, DCs, etc.).
Add destination-based steering exceptions
(hostname or IP+Port) for those destinations (see
Destination-Based Steering Exceptions
).
Ensure all user groups on the same VDA server share the same steering configuration
Group users by access profile on separate VDA server pools where possible.
Test and validate end-to-end: SMB access, printing, AD auth, profile loading.
Review security impact of destination bypasses (see
Security Impact of Destination-Based Bypass
) and apply network-level mitigations.
Monitor npadebug.log for policy mismatches or dropped connections.
Traffic Flow Diagram
References
Use the NPA Client in Windows Multi-User Virtual Desktop Environments
ZTNA Policy Best Practices for Session 0 (VDI Tunnel User)
Citrix ICA Virtual Channels Architecture
In this Topic
Citrix VDI Considerations for Netskope Private Access (NPA)

---
## Privileged Remote Access (PRA)
**URL:** https://docs.netskope.com/en/private-access-pra/
**Last Modified:** 2026-07-16T22:08:49+00:00
**Scraped:** 2026-09-03T11:20:11.464401+00:00

Privileged Remote Access (PRA) - Netskope Technical Documentation
Privileged Remote Access (PRA)
Privileged Remote Access (PRA) enables secure, clientless browser access to RDP and SSH applications with policy-based session governance and just-in-time credential injection.
Use PRA to:
Provide administrators and third parties with controlled RDP/SSH access without a VPN client.
Record privileged sessions for audit and compliance.
Inject vaulted credentials so end users never see passwords or keys.
Prerequisites
Netskope Private Access is enabled in your tenant.
Target RDP and SSH applications are defined as private app segments in NPA.
Real-time Protection (RTP) policies
are configured to allow access to those private app segments.
How PRA Works
RTP policies decide whether a user can access a private app segment (allow/deny).
PRA policies apply session-level controls to sessions that are already allowed.
PRA can:
Record or not record sessions for specific users/groups and apps/tags.
Inject credentials for specific users/groups and apps/tags.
Both RTP and PRA policies are evaluated in their own policy lists.
Access decision: RTP policy
Session governance: PRA policy (session recording and credential injection)
Configure PRA Policies
Go to
Policies > Private Access > Privileged Remote Access Control
.
Create a PRA Policy
Click
New Policy
. You are prompted to choose a policy type:
Session Governance
: Governing privileged RDP/SSH sessions. Use this type to control whether sessions are recorded.
Credential Injection
: Enable privileged RDP/SSH credential injection. Use this type to inject vaulted credentials into sessions.
Under
Criteria
(all criteria sections are AND’ed together):
Source
: Select the users or groups.
Destination
: Select
Private App Segments
/tags.
Under
Action
:
For a
Session Governance
policy: toggle
Record Session
on or off.
For a
Credential Injection
policy: select the
Credential Object
to inject.
Under
General
:
Enter a
Name
and optional
Description
.
Set
Policy Position
to control evaluation order.
Set
Status
to Enabled.
Configure Credential Objects
Before you can configure credential injection in a PRA policy, you must create one or more credential objects. A credential object stores the privileged RDP or SSH credentials in the Netskope Vault so they can be automatically injected into sessions.
Create a Credential Object
Go to
Policies > Profiles > Privileged Remote Access Control Credentials
.
Click
New Credential
. A side panel opens with the following fields:
Credential Object Name
(required): A descriptive name for this credential (for example,
Windows Admin RDP
or
Linux Root SSH
).
Description
(optional): Additional context about the credential.
Vault
: Select
Netskope
(default).
Type
: Choose
RDP
or
SSH
:
If RDP is selected:
Username
(required)
Password
(required, masked with show/hide toggle)
Domain
(optional)
If SSH is selected
, choose an authentication method:
Password
: Enter
Username
(required) and
Password
(required, masked).
Private Key
: Enter
Username
(required), paste or upload the
Private Key
, and optionally enter a
Passphrase
.
Click
Save
. The credential object appears in the credentials listing table.
Edit a Credential Object
On the
Privileged Remote Access Control Credentials
page, locate the credential card.
Click the three-dot menu (⋮) on the card and select
Edit
.
Update the fields as needed and click
Save
.
Delete a Credential Object
Click the three-dot menu (⋮) on the credential card and select
Delete
.
Confirm the deletion.
Note:
You cannot delete a credential object that is currently linked to a PRA policy. Remove the credential from any associated policies before deleting it.
Verify PRA Behavior
Use the configured access method (for example, Browser Access or Enterprise Browser) to launch the RDP/SSH app.
Verify the user successfully reaches the target app.
If recording is enabled, check for any recording indicator in the session UI.
If credential injection is enabled, verify the session establishes without the user manually entering credentials (when configured that way).
Validation
Go to
Events > Network Events
.
Filter for PRA-related events.
Open the event for the test session and confirm:
The action reflects the expected PRA policy.
A recording download is available when session recording is enabled (after processing completes).
FAQs
Does PRA policy replace existing RTP access policy?
No, RTP policies continue to control allow/deny decisions; PRA policies add session-level controls on top of already-allowed sessions.
Can I apply both recording and credential injection to the same app segment?
Yes, you can configure separate policies for the same app segment: one for session governance to enforce recording and another for credential injection.
Do users ever see the injected credentials?
No, credentials are not exposed to end users.
In this Topic
Privileged Remote Access (PRA)

---
## Private Access AIOps Agent - Netskope Technical Documentation
**URL:** https://docs.netskope.com/en/private-access-aiops-agent/
**Last Modified:** 2026-07-24T19:38:36+00:00
**Scraped:** 2026-09-03T11:21:39.192436+00:00

Private Access AIOps Agent - Netskope Technical Documentation

---
## Private Access AIOps Agent
**URL:** https://docs.netskope.com/en/private-access-ai-ops-agent/
**Last Modified:** 2026-09-02T22:01:40+00:00
**Scraped:** 2026-09-03T11:21:43.809323+00:00

Private Access AIOps Agent - Netskope Technical Documentation
Private Access AIOps Agent
The Private Access AIOps Agent:
Generates Application Segments and Real-time policies.
Audits existing Application Segments.
Generate Application Segments and Real-time Policies
Use the Private Access AIOps Agent to generate narrow Application Segments and associated Real-time policies for least privileged access.
Prerequisite
Baseline NPA Real-time policies to access Application Segments containing IP subnets or wildcard domains.
Procedure
In your Netskope tenant, go to
Settings > Security Cloud Platform > App Definition
and click
Private App Segments
.
Click
Set Up App Segment Generation Agent
.
On the
Generate App Segments and Policies
tab, click
+ Add New
. Scope setup does not grant access. Ensure that a policy already exists to allow access from Source to Destinations specified in App Segments.
Select a policy from the dropdown of existing NPA policies. The AIOps Agent will limit its generation Scope to Source and Destination criteria present in the selected policy.
Click
Create Scope
.
Enter and select these parameters:
Source
: Entries are imported from the policy selected in the previous step. It is possible to remove entries.
Note
Source criteria specifies the users/AD groups that the NPA Agent should include for analysis. If the Source field is left blank, the Agent will consider the entire set of users who have access to the specified App Segments. Alternatively, a subset of AD groups corresponds to a more specific scope.
Adding source criteria that is not present in the original NPA policy is not recommended.
App Segment
: Entries are imported from the policy selected in the previous step. It is possible to remove entries.
Note
Adding an Application Segment that is not present in the original NPA policy is not recommended.
AI Agent will only evaluate Application Segments that have Access Method set to Client.
Customized Name
: Provide a text string. The AIOps Agent will add this string at the start of all  Application Segments that are generated for this scope.
Protocol & Port:
By default, the AIOps agent will generate Application Segments to include all protocols and ports (1-65535). Optionally, if you want to limit the scope to a specific set of protocols and ports, select from them from the dropdown, or manually specify them using the
Enter additional ports
option.
Policy Granularity
: By default, the AIOps agent generates least privilege policies to cover an aggregated set of users or user groups. This is recommended for replacing a broad policy with a narrower one. Optionally, if you would like AIOps agent to generate a granular policy for each user or user group, enable the
Least privilege policy for each user or user group
option
.
Maximum User Count in Source Criteria
: This field controls the maximum count of individual users that the AIOps agent should display in the Source criteria of the generated policy. If the count of  observed users exceeds the specified value, the AIOps agent will instead use the closest Active Directory group as the Source criteria of the generated policy. The default and lowest value is 5 and the
maximum value is 20.
Click
Save
.
Specify the scopes for the AIOps agent to evaluate, and click
Start Generation
.
Click
Proceed
.
On the App Definition page, click
Review Recommendations
.
App Segment
: Entries are imported from the policy selected in the previous step. It is possible to remove entries.
The
AIOps Agent Recommendations
page opens for the Scope just created and shows:
The Scope name.
The number of Generated Policies and Generated Application Segments, plus the number and percentage for each that Needs Review, are Approved, or Ignored.
The current status of this scope (in this case, Needs Review)
The name and details of the new Policy.
The names and details of the new Application Segments.
A
Show Reasoning
button that provides more specifics about the recommendations.
Source: The Source field represents the list of users, AD groups or OU that require access to the generated Application Segments.
Multiple entries in Source Group represent Active Directory groups and indicate that users across these AD groups have access to destinations present in the Application Segments.
Click on one of the new Application Segments to see its configuration details.
Note
In the generated Application Segment, AI Agent will include all the publishers from the top level App Segment that was specified in the Scope configuration, even if the additional Publishers did not connect users to applications during the time frame specified for generation.
Furthermore, Agent will exclude deleted Application Segments and policies for its analysis.
AI Agent will exclude user activity to Applications, if the access was not successful. The unsuccessful attempt corresponds to
Packets Received:0
in the
Network Event
for the requested Application.
To proceed with the recommended changes, click the green checkmark icon for the Policy. To ignore the recommendations, click the red x icon.
Review the recommended changes, and then click
Approve and Save
.
Click
Apply Changes
.
Go to the respective page to view the new Application Segments (
Settings > Security Cloud Platform > App Definition >
Private App Segments
) and (
Policies > Real-time Protection
)
Audit Application Segments
Use the Private Access AIOps Agent to audit and get recommendations for existing Application Segments within the tenant. The AIOps Agent’s audit tasks include:
Replacing broad network destinations and wildcard domains with narrower IP subnets or precise IP destinations and FQDNs in existing application definitions.
Identifying and removing unused destinations and ports.
Procedure
In your Netskope tenant, go to
Settings > Security Cloud Platform > App Definition
and click
Private App Segments
.
Click
Start Audit
.
Click
Run Analysis
.
For tenants with AI Agent entitlement, the Agent will look back at data up to 12 months from the Analysis task initiation date.
The Audit Summary page opens.
Click an Application Segment. Recommendations are shown in a table.
There are two tabs, Destinations and Ports.
You can perform these actions:
Approve
: Performs the recommendation stated, like removing or replacing destinations and ports.
When you click
Approve
, a Confirm Change box opens. Review the change and click
Approve & Save
.
Ignore
: Labels the recommendation as ignored, and no change is made.
In the event that you want to change this back, click
Revert
.
Preview
: Provides specific details about the recommendation.
Review the changes and click
Approve & Save
(or
Ignore
to not make this change).
Confirm the changes and click
Approve & Save
again.
Edit notes
: Opens the Notes for this recommendation so you can add pertinent information.
Enter the information you want add for this recommendation, and then click
Save
.
When you are finished, the Recommendation will show as
Review Completed
on the Audit Summary page. Incomplete Reviews show as
Under Review
.
After an Audit is performed, the Private App Segments App Definition page will show that there are recommendations to view and the day the Audit was performed.
Audit Summary Page Functions
When viewing audit summaries, you have these options:
Filters
: You can search for an Private App Segment by name, sort by most or least recommendations, and see according to status.
Export
: Click
Export
to download a zip file with audit results in CSV files.
View the CSV files for detailed metrics.
Recommendations Page Functions
When viewing Recommendations, you can sort by Recommendation and Action Status.
Admin Notifications
To notify users about the changes, go to the
Admin Notifications
tab. This will send an email notification when the AI Agent has completed a task to all the users listed.
To add more recipients, click select and add them. When finished, click
Save
.
In this Topic
Private Access AIOps Agent

---
## Netskope One Private Access Licensing Terms
**URL:** https://docs.netskope.com/en/netskope-one-private-access-licensing-terms/
**Last Modified:** 2026-08-25T22:20:51+00:00
**Scraped:** 2026-09-03T11:21:59.579637+00:00

Netskope One Private Access Licensing Terms - Netskope Technical Documentation
Netskope One Private Access Licensing Terms
Service Description
Netskope One Private Access (NPA) inspects and enforces policy on user traffic transiting the Netskope NewEdge network, providing visibility and access control across a customer’s private application traffic.
Definitions and Units of Measure
A
User
is defined as each individual that (a) is authorized by the customer to use the customer’s systems (including the customer’s network, cloud services and Internet connections), and (b) whose use of such systems is monitored by, or accessed by use of, the Services.
A
Light User
means a User with the capacity restrictions set forth in the Licensing Model section below.
An
Application Segment
refers to a single Private Application definition configured in the Netskope console by the administrator.
Units of Measure
User & Light User
:
Each User or Light User counts as one Subscription Unit and cannot be shared between multiple Users.
Application Segments
: Each Private Application definition counts as one Application Segment.
Entitlement
Subscription Period:
As set forth in a customer’s order.
Licensing Model
User-Based
: Each Subscription Unit entitles the customer to one (1) User and the Subscription Unit cannot be shared across users. The Application Segment allocation across different NPA packages is specified in the Netskope quotation.
Light Users are entitled to a maximum of 5 Application Segments and 100 MB of traffic per Light User per month.
Pooling
: User and Application Segment entitlement is assigned at the account level and may be shared across multiple of the customer’s tenants, excluding Light Users.
Add-On Packages
: Customers may purchase incremental Subscription Units to increase their entitlements for Users or Application Segments (via “add-on” packages) at any time during the Subscription Period, by placing an additional Order.
Usage Monitoring
Customers may monitor their User and Application Segment count and retrieve a list of Users or Application Segments in their Netskope tenant Web UI at the tenant level. Netskope will also notify the customer via the account team when the number of Users or Application Segments exceeds the licensed quantity.
Measurement and Enforcement
Measurement Methodology
Netskope measures User usage based on the number of unique Users observed over a rolling 90-day period.
Netskope measures Application Segment usage based on the number of unique Application Segments existing on the observation date.
Service Limitations
: If service usage exceeds the purchased entitlement, Netskope may limit functionality until the customer acquires additional licenses.
Overage Remediation
: For Users and Application Segments, if the customer’s number of Users or Application Segments exceeds the purchased entitlement, the customer must, within 30 days of notification:
License additional User and/or Application Segment packages sufficient to cover the excess Users for the remainder of the Subscription Period.
Cease usage of the services by Users in excess of purchased User quantities.
Reduce the count of Application Segments in excess of purchased Application Segment quantities.
During the Service subscription period, Netskope will determine if actual Light Users exceed the capacity limitations set forth in the applicable product description. If actual capacity for any Light Users exceeds the capacity limitation, the customer is required within 30 days after notice to either:
Purchase upgrades to Users for all Light Users exceeding the capacity limitations.
Immediately cease utilization of the excess capacity for all Light Users exceeding the purchased quantity, or a combination of both.
Customer Records
: The customer may be required to provide written information or confirmation of the number of Users and Application Segments upon reasonable request by Netskope.
In this Topic
Netskope One Private Access Licensing Terms

---
## Netskope Private Access
**URL:** https://docs.netskope.com/en/netskope-private-access/
**Last Modified:** 2025-11-04T21:46:41+00:00
**Scraped:** 2026-09-03T11:23:14.896110+00:00

Netskope Private Access - Netskope Technical Documentation
Netskope Private Access
Netskope Private Access (NPA) offers a comprehensive solution that combines classic Zero Trust Network Access (ZTNA) for user-to-application flows with Layer 3 (L3) access for client-to-client and server-to-client interactions. This dual approach ensures secure, seamless, least-privileged access to applications, whether hosted in the cloud or on-premises, and supports workflows requiring direct communication like file sharing, remote desktop, and specialized applications.
By replacing legacy VPNs with a modern Zero Trust framework, Netskope Private Access enhances security with granular, context-aware controls, simplifies operations, and delivers comprehensive access coverage across all scenarios.
Netskope Private Access includes three subcomponents:
Netskope Private Application Access
(currently listed as
Netskope Private Access
in the UI): Supports all endpoint-initiated applications with a Zero Trust architecture, enabling secure, least-privileged access.
Netskope Private Optimized Access
(currently listed as
Netskope Endpoint SD-WAN
): Supports both endpoint- and server-initiated apps, offering VPN replacement with traffic optimization for improved performance.
Netskope Private Unified Access
: Combines the above components, offering full support for all app types with Zero Trust architecture.
This modular yet unified approach allows organizations to tailor secure access solutions while ensuring optimal scalability, security, and user experience.
Netskope Private Application Access
Netskope Private Application Access securely connects users to private applications in data centers or cloud environments using a Zero Trust architecture. It enforces least-privileged access and restricts users to only the applications they are authorized for—without exposing the broader network.
Key Features
Endpoint-Initiated Access
: Supports all apps launched from user devices.
Zero Trust Enforcement
: Validates identity, device posture, and application-specific permissions.
Granular Policy Controls
: Enables precise access management at the application level.
Cloud-Native Architecture
: Replaces traditional VPNs for faster, secure access.
TLS 1.2 Encryption
: All communication tunnels between Client and Publisher are encrypted using TLS 1.2 to ensure data confidentiality and integrity.
Advanced Threat Protection
: Using Netskope’s IPS and TSS Malware Protection capabilities.
Use Cases
Remote Workforce and BYOD
: Secure access to private apps from any device without VPNs.
Third-Party Access
: Granular, role-based access for contractors and partners.
Mergers and Acquisitions
: Rapid, secure integration of newly acquired users.
Cloud Migrations
: Maintain secure app access during migration.
Compliance and Auditing
: Meet regulatory requirements with detailed visibility.
Legacy System Access
: Modern VPN replacement for on-prem legacy apps
How It Works
Netskope Private Application Access operates through the seamless integration of the Private Access Broker and the Publisher to enforce Zero Trust principles and provide secure access. The Private Access Broker functions as a cloud-native control plane that validates user identity, device posture, and access policies in real time before granting access to applications.
The Publisher, a lightweight connector deployed on-premises or in the cloud, establishes secure, encrypted communication between users and private applications without exposing applications to the internet. This architecture ensures that users gain access only to the specific applications they are authorized to use, with optimized routing and granular control, while eliminating the need for traditional VPNs. This combination provides a highly secure, scalable, and efficient access solution for endpoint-initiated workflows.
NPA is illustrated in this diagram:
To watch a video about configuring Netskope Private Application Access, click play:
Prerequisites
In order to configure private apps with a Publisher, you need to:
Purchase the Netskope Private Access license and contact Support to have it enabled in your tenant.
Choose a private app to be published.
Collect information about the app: host, port(s).
Identify the network on which the app is running.
Using a modern release that is inline with our support policy.
For Publisher requirements and recommendations, plus OS hardening information, go to:
Deploy a Publisher
.
Supported Browsers
NPA has been tested on these browsers:
Google Chrome Version 92.0.4515.159 (Official Build) (x86_64) on Big Sur
Google Chrome Version 92.0.4515.159 (Official Build) (x86_64) on Mojave
Safari Version 14.1.2 (14611.3.10.1.5) on Mojave
Brave Version 1.26.67 Chromium: 91.0.4472.114 (Official Build) (x86_64)
Chrome Version 92.0.4515.159 (Official Build) (x86_64) on Catalina
Firefox 91.0.1 (64-bit) (on Mac Catalina)
Edge Version 80.0.361.69 (Official build) (64-bit)
Microsoft Edge Version 92.0.902.78 (Official build) (64-bit) Windows 10
iOS Use with Netskope Private Access
Netskope is replacing the existing iOS App for NPA (Netskope Private Access) with a new iOS App that supports NPA/CASB/SWG/CFW. This new unified iOS Client is called
Netskope Client
in the app store, and is intended to offer all the Netskope security services in a single client for iOS phones and tablets (iPads).
Important
Netskope ends the existing NPA iOS Netskope Client support with the new app released in release 102.0.0. With this end of support, you need to remove the existing NPA Netskope Client from all your iOS phones and tablets (iPads), and install the new Netskope Client from the store.
To learn more:
Netskope Client for iOS
.
Workflow
You can grant access to multiple private apps by repeating the following steps:
Create a publisher.
Deploy the publisher on your network.
Create a private app.
Steer traffic for the private app.
Add users.
Create policies so users can access a private app.
Deploy the Netskope Client on devices.
View Private Apps and Network Events information in Skope IT.
Note
The same publisher can be used to give access to multiple apps which resides on the same network.
If you need private apps in different networks (which are not routable from one to another), you will need to repeat these steps for each:
Create a publisher.
Deploy a publisher.
Netskope Private Optimized Access
Netskope Private Optimized Access (currently known in the UI as Netskope Endpoint SD-WAN) provides real-time visibility and optimization for all applications while ensuring consistent policy enforcement for employees connecting from any location, whether remote or on-premises.
Capabilities of Netskope Private Optimized Access
1. Bi-directional Flows
Provides both
client-to-server
and
server-to-client
traffic flows, enabling peer-to-peer communication, including legacy on-premises hosted VoIP solutions.
With dynamic traffic steering and context-aware QoS, it overcomes network performance challenges, boosting productivity for remote call center employees by ensuring an optimal voice and video application experience.
2. Server-to-Client Flows
Supports legacy applications that require server-initiated traffic, also known as
inside-out connectivity
,
where the traffic is endpoint-initiated.
Streamlines IT operations by supporting tools such as
Microsoft Remote Assistance
and
TeamViewer
for remote access, control, and support.
Further information on how to configure the private Optimized Access is here :
https://netskope.document360.io/
.
The following sections explain how to configure and use Private Access.
Private Access AIOps Agent
Publisher Management
Private App Management
Local Broker Management
Create a Real-time Protection Policy for Private App Segments
View Private App Segments and Network Events in Skope IT
Deploy the Netskope Client for Netskope Private Access
Private Access Troubleshooting
Private Access FAQs
Private Access Best Practices
Private Access REST APIs
Netskope Private Access for Microsoft Active Directory Domain Services
Netskope Private Access for SMB and DFS Services
Source IP Anchoring for an IdP with Netskope Private Access
NewEdge Traffic Management Zones per NPA Tenant
In this Topic
Netskope Private Access

---
## Netskope Private Access Publisher Release Notes Version 1.4.6431
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-1-4-6431/
**Last Modified:** 2025-08-31T02:03:16+00:00
**Scraped:** 2026-09-03T11:26:49.098387+00:00

Netskope Private Access Publisher Release Notes Version 1.4.6431 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 1.4.6431
Document Version: 1.1
Software Version: 1.4.6431
General Availability Date: October, 2021
What's New
Fixed Issues
Known Issues

---
## Netskope Private Access Publisher Release Notes Version 1.4.6526
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-1-4-6526/
**Last Modified:** 2025-08-31T02:03:12+00:00
**Scraped:** 2026-09-03T11:26:51.275784+00:00

Netskope Private Access Publisher Release Notes Version 1.4.6526 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 1.4.6526
Document Version: 1.0
Software Version: 1.4.6526
General Availability Date: December, 2021
What's New
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 1.4.6620
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-1-4-6620/
**Last Modified:** 2025-08-31T02:03:10+00:00
**Scraped:** 2026-09-03T11:26:52.357981+00:00

Netskope Private Access Publisher Release Notes Version 1.4.6620 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 1.4.6620
Document Version: 1.0
Software Version: 1.4.6620
General Availability Date: January, 2022
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 102.0.0.7784
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-102-0-0-7784/
**Last Modified:** 2025-08-31T02:02:47+00:00
**Scraped:** 2026-09-03T11:26:53.446160+00:00

Netskope Private Access Publisher Release Notes Version 102.0.0.7784 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 102.0.0.7784
Document Version: 1.0
Software Version: 102.0.0.7784
General Availability Date: March, 2023
What's New
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 101.0.0.7619
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-101-0-0-7619/
**Last Modified:** 2025-08-31T02:02:51+00:00
**Scraped:** 2026-09-03T11:26:54.535234+00:00

Netskope Private Access Publisher Release Notes Version 101.0.0.7619 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 101.0.0.7619
Document Version: 1.0
Software Version: 101.0.0.7619
General Availability Date: February, 2023
What's New

---
## Netskope Private Access Publisher Release Notes Version 1.4.6715
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-1-4-6715/
**Last Modified:** 2025-08-31T02:03:08+00:00
**Scraped:** 2026-09-03T11:26:55.861978+00:00

Netskope Private Access Publisher Release Notes Version 1.4.6715 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 1.4.6715
Document Version: 1.0
Software Version: 1.4.6715
General Availability Date: February, 2022
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 105.0.0.8080
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-105-0-0-8080/
**Last Modified:** 2025-08-31T02:02:32+00:00
**Scraped:** 2026-09-03T11:26:56.947468+00:00

Netskope Private Access Publisher Release Notes Version 105.0.0.8080 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 105.0.0.8080
Document Version: 1.0
Software Version: 105.0.0.8080
Supported Publisher Version: 105.0.0.8080,104.0.0.7933,103.0.0.7843, 102.0.0.7784
General Availability Date: June, 2023
Since this version includes minor bug fixes and enhancements, the release notes does not have a dedicated new features/enhancement and fixed version topics.

---
## Netskope Private Access Publisher Release Notes Version 104.0.0.7933
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-104-0-0-7933/
**Last Modified:** 2025-08-31T02:02:36+00:00
**Scraped:** 2026-09-03T11:26:58.032854+00:00

Netskope Private Access Publisher Release Notes Version 104.0.0.7933 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 104.0.0.7933
Document Version: 1.0
Software Version: 104.0.0.7933
Supported Publisher Version: 104.0.0.7933,103.0.0.7843, 102.0.0.7784, 101.0.0.7619
General Availability Date: May, 2023
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 103.0.0.7843
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-103-0-0-7843/
**Last Modified:** 2025-08-31T02:02:41+00:00
**Scraped:** 2026-09-03T11:26:59.121001+00:00

Netskope Private Access Publisher Release Notes Version 103.0.0.7843 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 103.0.0.7843
Document Version: 1.0
Software Version: 103.0.0.7843
Supported Publisher Version: 103.0.0.7843, 102.0.0.7784, 101.0.0.7619, 99.0.0.7505
General Availability Date: April, 2023
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 94.0.0.6867
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-94-0-0-6867/
**Last Modified:** 2025-08-31T02:03:00+00:00
**Scraped:** 2026-09-03T11:27:00.215572+00:00

Netskope Private Access Publisher Release Notes Version 94.0.0.6867 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 94.0.0.6867
Document Version: 1.0
Software Version: 94.0.0.6867
General Availability Date: April, 2022
What's New
Known Issues

---
## Netskope Private Access Publisher Release Notes Version 95.0.0.7066
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-95-0-0-7066/
**Last Modified:** 2025-08-31T02:03:05+00:00
**Scraped:** 2026-09-03T11:27:01.308438+00:00

Netskope Private Access Publisher Release Notes Version 95.0.0.7066 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 95.0.0.7066
Document Version: 1.0
Software Version: 95.0.0.7066
General Availability Date: June, 2022
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 97.0.0.7294
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-97-0-0-7294/
**Last Modified:** 2025-08-31T02:03:03+00:00
**Scraped:** 2026-09-03T11:27:02.420836+00:00

Netskope Private Access Publisher Release Notes Version 97.0.0.7294 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 97.0.0.7294
Document Version: 1.0
Software Version: 97.0.0.7294
General Availability Date: August, 2022
What's New

---
## Netskope Private Access Publisher Release Notes Version 96.0.0.7170
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-96-0-0-7170/
**Last Modified:** 2025-08-31T02:03:07+00:00
**Scraped:** 2026-09-03T11:27:03.506493+00:00

Netskope Private Access Publisher Release Notes Version 96.0.0.7170 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 96.0.0.7170
Document Version: 1.0
Software Version: 96.0.0.7170
General Availability Date: July, 2022
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 98.1.0.7432
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-98-1-0-7432/
**Last Modified:** 2025-08-31T02:02:57+00:00
**Scraped:** 2026-09-03T11:27:04.594789+00:00

Netskope Private Access Publisher Release Notes Version 98.1.0.7432 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 98.1.0.7432
Document Version: 1.0
Software Version: 98.1.0.7432
General Availability Date: September, 2022
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 98.0.0.7378
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-98-0-0-7378/
**Last Modified:** 2025-08-31T02:03:02+00:00
**Scraped:** 2026-09-03T11:27:05.681709+00:00

Netskope Private Access Publisher Release Notes Version 98.0.0.7378 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 98.0.0.7378
Document Version: 1.0
Software Version: 98.0.0.7378
General Availability Date: September, 2022
What's New

---
## Netskope Private Access Publisher Release Notes Version 99.0.0.7505
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-99-0-0-7505/
**Last Modified:** 2025-08-31T02:02:54+00:00
**Scraped:** 2026-09-03T11:27:06.768400+00:00

Netskope Private Access Publisher Release Notes Version 99.0.0.7505 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 99.0.0.7505
Document Version: 1.0
Software Version: 99.0.0.7505
General Availability Date: October, 2022
What's New

---
## Netskope Private Access Publisher Release Notes Version 106.0.0.8102
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-106-0-0-8102/
**Last Modified:** 2025-08-31T02:02:56+00:00
**Scraped:** 2026-09-03T11:29:25.141511+00:00

Netskope Private Access Publisher Release Notes Version 106.0.0.8102 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 106.0.0.8102
Document Version: 1.0
Software Version: 106.0.0.8102
General Availability Date: July, 2023
Supported Publisher Version: 106.0.0.8102, 105.0.0.8080, 104.0.0.7933, 103.0.0.7843
What's New

---
## Netskope Private Access Publisher Release Notes Version 107.0.0.8134
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-107-0-0-8134/
**Last Modified:** 2025-08-31T02:02:52+00:00
**Scraped:** 2026-09-03T11:29:47.037348+00:00

Netskope Private Access Publisher Release Notes Version 107.0.0.8134 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 107.0.0.8134
Document Version: 1.0
Software Version:107.0.0.8134
Supported Publisher Version: 107.0.0.8134, 106.0.0.8102, 105.0.0.8080, 104.0.0.7933
General Availability Date: August, 2023
What's New

---
## Netskope Private Access Publisher Release Notes Version 108.0.0.8181
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-108-0-0-8181/
**Last Modified:** 2025-08-31T02:02:49+00:00
**Scraped:** 2026-09-03T11:30:03.748280+00:00

Netskope Private Access Publisher Release Notes Version 108.0.0.8181 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 108.0.0.8181
Document Version: 1.0
Software Version:  108.0.0.8181
Supported Publisher Version:  108.0.0.8181, 107.0.0.8134, 106.0.0.8102, 105.0.0.8080
General Availability Date: September, 2023
What's New

---
## Netskope Private Access Publisher Release Notes Version 110.0.0.8301
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-110-0-0-11012023/
**Last Modified:** 2025-08-31T02:02:43+00:00
**Scraped:** 2026-09-03T11:30:37.520838+00:00

Netskope Private Access Publisher Release Notes Version 110.0.0.8301 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 110.0.0.8301
Document Version: 1.0
Software Version:  110.0.0.8301
Supported Publisher Version:  110.0.0.8301, 109.0.0.8228, 108.0.0.8181, 107.0.0.8134
General Availability Date: November, 2023
Release Notes Publishing Date: November 10, 2023
What's New
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 112.0.0.8440
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-112-0-0-8440/
**Last Modified:** 2025-08-31T02:02:35+00:00
**Scraped:** 2026-09-03T11:31:20.356235+00:00

Netskope Private Access Publisher Release Notes Version 112.0.0.8440 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 112.0.0.8440
Document Version: 1.0
Software Version:  112.0.0.8440
Supported Publisher Version:  112.0.0.8440, 111.0.0.8350, 110.0.0.8301, 109.0.0.8228
General Availability Date: February 8, 2024
Release Notes Publishing Date: February 8, 2024
What's New
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 113.0.0.8462
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-113-0-0-8462/
**Last Modified:** 2025-08-31T02:02:31+00:00
**Scraped:** 2026-09-03T11:31:31.247417+00:00

Netskope Private Access Publisher Release Notes Version 113.0.0.8462 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 113.0.0.8462
Document Version: 1.0
Software Version: 113.0.0.8462
Supported Publisher Version: 113.0.0.8462, 112.0.0.8440, 111.0.0.8350
General Availability Date: March 12, 2024
Release Notes Publishing Date: March 12, 2024
New Features and Enhancements in Publisher Version 113.0.0.8462
What's New

---
## Netskope Private Access Publisher Release Notes Version 114.0.0 (Skip release)
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-114-0-0-skip-release/
**Last Modified:** 2025-08-31T02:02:30+00:00
**Scraped:** 2026-09-03T11:31:49.860746+00:00

Netskope Private Access Publisher Release Notes Version 114.0.0 (Skip release) - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 114.0.0 (Skip release)
There are no Publisher updates for version 114. Continue to use
version 113
as the latest release.

---
## Netskope Private Access Publisher Release Notes Version 115.0.0.8634
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-115-0-0-8634/
**Last Modified:** 2025-08-31T02:02:29+00:00
**Scraped:** 2026-09-03T11:32:04.377847+00:00

Netskope Private Access Publisher Release Notes Version 115.0.0.8634 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 115.0.0.8634
Document Version: 1.0
Software Version: 115.0.0.8634
Supported Publisher Versions: 115.0.0.8634, 113.0.0.8462, 112.0.0.8440
General Availability Date: May 9, 2024
Release Notes Publishing Date: May 9, 2024
What's New
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 116.0.0.8665
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-116-0-0-8665/
**Last Modified:** 2025-08-31T02:02:26+00:00
**Scraped:** 2026-09-03T11:32:24.063609+00:00

Netskope Private Access Publisher Release Notes Version 116.0.0.8665 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 116.0.0.8665
Document Version: 1.0
Software Version: 116.0.0.8665
Supported Publisher Versions: 116.0.0.8665, 115.0.0.8634, 113.0.0.8462
General Availability Date: June 10, 2024
Release Notes Publishing Date: June 10, 2024
What's New

---
## Netskope Private Access Publisher Release Notes Version 117.0.0.8690
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-117-0-0-8690/
**Last Modified:** 2025-08-31T02:02:25+00:00
**Scraped:** 2026-09-03T11:32:42.627618+00:00

Netskope Private Access Publisher Release Notes Version 117.0.0.8690 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 117.0.0.8690
Document Version: 1.0
Software Version:
117.0.0.8690
Supported Publisher Versions:
117.0.0.8690, 116.0.0.8665, 115.0.0.8634
General Availability Date: July 10, 2024
Release Notes Publishing Date: July 10, 2024
What's New

---
## Netskope Private Access Publisher Release Notes Version 118.0.0.8741
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-118-0-0-8741/
**Last Modified:** 2025-08-31T02:02:23+00:00
**Scraped:** 2026-09-03T11:33:09.829687+00:00

Netskope Private Access Publisher Release Notes Version 118.0.0.8741 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 118.0.0.8741
Document Version: 1.0
Software Version: 118.0.0.8741
Supported Publisher Versions: 118.0.0.8741, 117.0.0.8690, 116.0.0.8665
General Availability Date: August 19, 2024
Release Notes Publishing Date: August 19, 2024
What's New
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 119.0.0.8846
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-119-0-0-8846/
**Last Modified:** 2025-08-31T02:02:21+00:00
**Scraped:** 2026-09-03T11:33:25.740567+00:00

Netskope Private Access Publisher Release Notes Version 119.0.0.8846 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 119.0.0.8846
Document Version: 1.0
Software Version: 119.0.0.8846
Supported Publisher Versions: 119.0.0.8846, 118.0.0.8741, 117.0.0.8690
General Availability Date: September 9, 2024
Release Notes Publishing Date: September 9, 2024
What's New
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 120.0.0.8869
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-120-0-0-8869/
**Last Modified:** 2025-08-31T02:02:18+00:00
**Scraped:** 2026-09-03T11:33:40.518116+00:00

Netskope Private Access Publisher Release Notes Version 120.0.0.8869 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 120.0.0.8869
Document Version: 1.0
Software Version:
120.0.0.8869
Supported Publisher Versions:
120.0.0.8869, 1
19.0.0.8846, 118.0.0.8741
General Availability Date: October 9, 2024
Release Notes Publishing Date: October 9, 2024
What's New

---
## Netskope Private Access Publisher Release Notes Version 121.0.0.8953
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-121-0-0-8953/
**Last Modified:** 2025-08-31T02:02:17+00:00
**Scraped:** 2026-09-03T11:34:02.357105+00:00

Netskope Private Access Publisher Release Notes Version 121.0.0.8953 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 121.0.0.8953
Document Version: 1.0
Software Version:
121.0.0.8953
Supported Publisher Versions:
121.0.0.8953,
120.0.0.8869, 1
19.0.0.8846
General Availability Date: November 11, 2024
Release Notes Publishing Date: November 11, 2024
What's New

---
## Netskope Private Access Publisher Release Notes Version 122.0.0.9124
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-122-0-0-9124/
**Last Modified:** 2025-08-31T02:02:15+00:00
**Scraped:** 2026-09-03T11:34:15.412857+00:00

Netskope Private Access Publisher Release Notes Version 122.0.0.9124 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 122.0.0.9124
Document Version: 1.0
Software Version:
122.0.0.9124
Supported Publisher Versions:
122.0.0.9124,
121.0.0.8953,
120.0.0.8869
General Availability Date: December 9, 2024
Release Notes Publishing Date: December 9, 2024
What's New

---
## Netskope Private Access Publisher Release Notes Version 123.0.0.9194
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-123-0-0-9194/
**Last Modified:** 2025-08-31T02:02:13+00:00
**Scraped:** 2026-09-03T11:35:23.400443+00:00

Netskope Private Access Publisher Release Notes Version 123.0.0.9194 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 123.0.0.9194
Document Version: 1.0
Software Version:
123.0.0.9194
Supported Publisher Versions:
123.0.0.9194,
122.0.0.9124,
121.0.0.8953
General Availability Date: February 10, 2025
Release Notes Publishing Date: February 10, 2025
What's New

---
## Netskope Private Access Publisher Release Notes Version 124.0.0.9304
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-124-0-0-9304/
**Last Modified:** 2025-08-31T02:02:12+00:00
**Scraped:** 2026-09-03T11:35:34.331830+00:00

Netskope Private Access Publisher Release Notes Version 124.0.0.9304 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 124.0.0.9304
Document Version: 1.0
Software Version: 124.0.0.9304
Supported Publisher Versions: 124.0.0.9304,
123.0.0.9194,
122.0.0.9124
General Availability Date: March 14, 2025
Release Notes Publishing Date: March 14, 2025
What's New

---
## Netskope Private Access Publisher Release Notes Version 124.1.0.9370
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-124-1-0-9370/
**Last Modified:** 2025-08-31T02:02:10+00:00
**Scraped:** 2026-09-03T11:35:39.761991+00:00

Netskope Private Access Publisher Release Notes Version 124.1.0.9370 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 124.1.0.9370
Document Version: 1.0
Software Version: 124.1.0.9370
Supported Publisher Versions: 124.1.0.9370, 124.0.0.9304,
123.0.0.9194
General Availability Date: March 28, 2025
Release Notes Publishing Date: March 28, 2025
What's New
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 125.0.0.9474
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-125-0-0-9474/
**Last Modified:** 2025-08-31T02:02:08+00:00
**Scraped:** 2026-09-03T11:36:01.890258+00:00

Netskope Private Access Publisher Release Notes Version 125.0.0.9474 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 125.0.0.9474
Document Version: 1.0
Software Version: 125.0.0.9474
Supported Publisher Versions: 125.0.0.9474, 124.1.0.9370, 124.0.0.9304
General Availability Date: April 24, 2025
Release Notes Publishing Date: April 24, 2025
What's New
Known Issues

---
## Netskope Private Access Publisher Release Notes Version 126.0.0.9487
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-126-0-0-9487/
**Last Modified:** 2025-08-31T02:02:05+00:00
**Scraped:** 2026-09-03T11:36:13.932304+00:00

Netskope Private Access Publisher Release Notes Version 126.0.0.9487 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 126.0.0.9487
Document Version: 1.0
Software Version: 126.0.0.9487
Supported Publisher Versions: 126.0.0.9487, 125.0.0.9474, 124.1.0.9370
General Availability Date: May 12, 2025
Release Notes Publishing Date: May 12, 2025
What's New

---
## Netskope Private Access Publisher Release Notes Version 128.0.0.9857
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-128-0-0-9857/
**Last Modified:** 2025-08-31T02:02:03+00:00
**Scraped:** 2026-09-03T11:36:56.433532+00:00

Netskope Private Access Publisher Release Notes Version 128.0.0.9857 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 128.0.0.9857
Document Version: 1.0
Software Version: 128.0.0.9857
Supported Publisher Versions: 128.0.0.9857, 126.0.0.9487, 125.0.0.9474
General Availability Date: July 15, 2025
Release Notes Publishing Date: July 15, 2025
What's New

---
## Netskope Private Access Publisher Release Notes Version 129.0.0.10054
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-129-0-0-10054/
**Last Modified:** 2025-08-31T02:02:01+00:00
**Scraped:** 2026-09-03T11:37:17.528874+00:00

Netskope Private Access Publisher Release Notes Version 129.0.0.10054 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 129.0.0.10054
Netskope Private Access Publisher Release Notes Version
129.0.0.10054
Document Version: 1.0
Software Version: 129.0.0.10054
Supported Publisher Versions: 129.0.0.10054, 128.0.0.9857, 126.0.0.9487
General Availability Date: August 12, 2025
Release Notes Publishing Date: August 12, 2025
What's New
Fixed Issues

---
## Netskope One Private Access Publisher Release Notes Version 130.0.0.10218
**URL:** https://docs.netskope.com/en/netskope-one-private-access-publisher-release-notes-version-130-0-0-10218/
**Last Modified:** 2025-09-08T20:25:45+00:00
**Scraped:** 2026-09-03T11:37:41.541480+00:00

Netskope One Private Access Publisher Release Notes Version 130.0.0.10218 - Netskope Technical Documentation
Netskope One Private Access Publisher Release Notes Version 130.0.0.10218
Netskope Private Access Publisher Release Notes Version
130.0.0.10218
Document Version: 1.0
Software Version: 130.0.0.10218
Supported Publisher Versions: 130.0.0.10218, 129.0.0.10054, 128.0.0.9857
General Availability Date: September 8, 2025
Release Notes Publishing Date: September 8, 2025
What's New
Fixed Issues

---
## Netskope One Private Access Publisher Release Notes Version 130.0.0.10218
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-netskope-one-private-access-publisher-version-130-0-0-10218/
**Last Modified:** 2025-09-08T20:39:46+00:00
**Scraped:** 2026-09-03T11:37:42.649284+00:00

Netskope One Private Access Publisher Release Notes Version 130.0.0.10218 - Netskope Technical Documentation
Netskope One Private Access Publisher Release Notes Version 130.0.0.10218
Netskope Private Access Publisher Release Notes Version
130.0.0.10218
Document Version: 1.0
Software Version: 130.0.0.10218
Supported Publisher Versions: 130.0.0.10218, 129.0.0.10054, 128.0.0.9857
General Availability Date: September 8, 2025
Release Notes Publishing Date: September 8, 2025
What's New
Fixed Issues

---
## Netskope One Private Access Publisher Release Notes Version 130.0.0.10218
**URL:** https://docs.netskope.com/en/fixed-issues-in-netskope-one-private-access-publisher-version-130-0-0-10218/
**Last Modified:** 2025-09-08T20:26:07+00:00
**Scraped:** 2026-09-03T11:37:43.735158+00:00

Netskope One Private Access Publisher Release Notes Version 130.0.0.10218 - Netskope Technical Documentation
Netskope One Private Access Publisher Release Notes Version 130.0.0.10218
Netskope Private Access Publisher Release Notes Version
130.0.0.10218
Document Version: 1.0
Software Version: 130.0.0.10218
Supported Publisher Versions: 130.0.0.10218, 129.0.0.10054, 128.0.0.9857
General Availability Date: September 8, 2025
Release Notes Publishing Date: September 8, 2025
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 131.0.0
**URL:** https://docs.netskope.com/en/netskope-one-private-access-release-notes-version-131-0-0/
**Last Modified:** 2025-12-05T02:34:22+00:00
**Scraped:** 2026-09-03T11:38:01.371166+00:00

Netskope Private Access Release Notes Version 131.0.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 131.0.0
Published on: October 16, 2025
We are excited to announce our Netskope One Private Access release updates! Find the latest features, issues fixed, and other updates in this release for Netskope One Private Access below.
Release Highlights
These are the highlights for this release:
Private Access Cloud
Private Applications across multiple Netskope tenants for macOS
.
Publisher
Dynamic Reconnection Based on Relative Latency
Browser Access AnyApp RDP/SSH Enhancements
.
Local Broker
Support pre-built Ubuntu 22.04 VM Hyper-V image for Local Brokers. Learn
more
.
Private Access Cloud Release Notes
Here are the latest updates with the Netskope Private Access UI.
New Features and Enhancements
Private Applications Across Multiple Netskope Tenants for macOS
Users can now access Private Applications across multiple Netskope tenants, such as from a managed service provider, partner or third-party organizations, without needing to unenroll or uninstall the Netskope Client for up to 20 different tenants. With a simple switch in the Client UI, users can toggle between their primary and partner tenants in one click.
Key Capabilities
:
Multi-Tenant Access
: Seamlessly switch between partner organizations to access authorized private resources.
Client UI Enhancements
: View current tenant details and a submenu listing all available partner tenants.
No Reinstallation Required
: Eliminates the need to unenroll/reinstall the Netskope Client when switching tenants.
Use Case Example:
Ideal for users working with suppliers, contractors, or joint ventures that also utilize Netskope, ensuring secure access to partner-hosted private applications without disruption.
Supported OS: macoS, Windows (supported from 125.0.0)
Supported minimum Client version:
125.0.0 (Windows), 131.0.0 (macOS)
This is a controlled General Availability feature. Contact Netskope Support or your Sales Representative to enable this feature for your tenant.
Dynamic Reconnection Based on Relative Latency
The Publisher will now periodically re-evaluate its connection to find the best-performing Point of Presence (PoP). This intelligent, dynamic reconnection ensures your system consistently uses the fastest and most reliable path available, improving overall performance and resilience against network degradation. This feature can be enabled in the Publisher Wizard.
Supported minimum Publisher version:
131.0.0
Fixed Issues
Issue Number
Description
722716
When cloning a Client configuration, Prelogon settings will be reset (Prelogon checkbox will be unchecked).
722908
Resolved a network routing issue that affected private application connections in environments with multiple local brokers. Some connections were incorrectly routed during failover scenarios, resulting in intermittent connection failures and sessions with no data transfer. This fix ensures consistent connectivity to private applications in multi-broker environments, improving reliability particularly during automatic failover events.
733159
When the Publisher Name contains characters like ‘#’, the Create App action for Discovered Apps in SkopeIT > Private Apps fails.
Reserved characters such as ‘#’ were not encoded, causing them to be removed from the URL when fetching Publisher details.
The fix encodes special characters like ‘#’ in the request.
733552
Resolved an issue where stale policies could be incorrectly applied to traffic after their parent policy group was deleted. In certain cases, private application policies created through our API were incorrectly processed for DLP traffic due to structural discrepancies. The fix ensures proper policy classification and prevents deleted or orphaned policies from affecting traffic evaluation, resulting in more accurate and predictable policy enforcement.
746325
Resolved an issue in China support-enabled tenants where NPA certificates stored incorrectly caused NPA gateway tunnel establishment to fail due to certificate verification errors.
Known Issues
Issue Number
Description
731748
The Toggle button for the Status is currently broken due to regression. Until it’s fixed, customers are advised to click on the pencil icon and toggle the status from the Edit Publisher Update Profile panel.
Publisher Release Notes
Here are the latest updates with the Netskope Private Access Publisher.
New Features and Enhancements
Updated Kernel Versions
Platform
Kernal Version
OVA
VHDX
AMI
VHD
5.15.0-156-generic
6.8.0-1034-azure
6.5.0-1024-aws
6.8.0-1034-azure
SHA Hash for Publisher Images
Image Type
SHA256
OVA
0e3f56467ec03cf4d494c82a143e0bec191bbf3245813e2ba66c17782498cc9d
VHDX
a23f1dd417e95743ead97ab6d5dd7ac76be72b4f2873a96c1a98cdec63bfeded
OVA/VHDX Hosting on the Alicloud
OVA hosting on the AliCloud:
https://npa-ova.oss-cn-shenzhen.aliyuncs.com/latest/NetskopePrivateAccessPublisher.ova
VHDX hosting on the AliCloud:
https://npa-ova.oss-cn-shenzhen.aliyuncs.com/latest/NetskopePrivateAccessPublisher.vhdx
Browser Access AnyApp RDP/SSH Enhancements
Enhanced RDP authentication
: AnyApp RDP now defaults to
Any
as the authentication method. This expands RDP authentication to support Active Directory domain integration and improves handling, ensuring more reliable connections for organizations using AD domain.
Clipboard controls
: Clipboard controls for RDP and SSH sessions allow precise management of data transfer between local and remote sessions. Organizations can configure clipboard access with these options:
Full clipboard access (copy and paste)
No clipboard access (block copy and paste).
Existing BA AnyApp tenants keep their current clipboard settings (disabled by default). New tenants have full clipboard enabled by default. To change this, contact Netskope support.
Non-English keyboard support
: Remote sessions now support multiple keyboard layouts in RDP sessions, letting international users keep their preferred configurations. This ensures consistent typing between local and remote environments worldwide. Notice that the local and remote must use the same keyboard language.
Improved user interface
: The RDP experience with Browser Access (BA) AnyApp features a more intuitive interface with clearer login instructions, visible session information (including Private App name and user details), and improved navigation and scrolling.
Improved Troubleshooter mTLS Check to Stitcher
Enhanced the troubleshooting process for mTLS checks related to the stitcher component.
Configure Daily Time Window when the Auto-reconnect is Active
Introduced a feature to configure a daily time window for auto-reconnect functionality. Users can now set specific times for when the auto-reconnect will be active.
Fixed Issues
Issue Number
Description
728329
This fix resolves connection failures in GSLB fallback blocks after GSLB resolution, enhancing reliability for Clients and Publishers.
Local Broker Release Notes
Here are the latest updates with the Netskope Private Access Local Broker.
New Features and Enhancements
Support pre-built Ubuntu 22.04 VM image for Hyper-V
NPA Local Broker now supports a pre-built Ubuntu 22.04 image in Hyper-V (VHDX) format

---
## Netskope Private Access Release Notes Version 132.0
**URL:** https://docs.netskope.com/en/netskope-private-access-release-notes-version-132-0/
**Last Modified:** 2025-12-05T01:38:50+00:00
**Scraped:** 2026-09-03T11:38:42.979855+00:00

Netskope Private Access Release Notes Version 132.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 132.0
Published on: December 4, 2025
We are excited to announce our Netskope Private Access release updates! Find the latest features, issues fixed, and other updates in this release for Netskope Private Access below.
Release Notes Subscription
Would you like to subscribe to our release notes? To learn more:
Release Notes Subscription
.
Upcoming Product Changes
To preview some of what’s coming in the next release, see:
Product Change Notification
.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 132.0
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-netskope-private-access-version-132-0/
**Last Modified:** 2025-12-05T20:47:48+00:00
**Scraped:** 2026-09-03T11:38:44.077951+00:00

Netskope Private Access Release Notes Version 132.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 132.0
Published on: December 4, 2025
We are excited to announce our Netskope Private Access release updates! Find the latest features, issues fixed, and other updates in this release for Netskope Private Access below.
Release Notes Subscription
Would you like to subscribe to our release notes? To learn more:
Release Notes Subscription
.
Upcoming Product Changes
To preview some of what’s coming in the next release, see:
Product Change Notification
.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 132.0
**URL:** https://docs.netskope.com/en/fixed-issues-in-netskope-private-access-version-132-0/
**Last Modified:** 2025-12-05T20:49:17+00:00
**Scraped:** 2026-09-03T11:38:45.162722+00:00

Netskope Private Access Release Notes Version 132.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 132.0
Published on: December 4, 2025
We are excited to announce our Netskope Private Access release updates! Find the latest features, issues fixed, and other updates in this release for Netskope Private Access below.
Release Notes Subscription
Would you like to subscribe to our release notes? To learn more:
Release Notes Subscription
.
Upcoming Product Changes
To preview some of what’s coming in the next release, see:
Product Change Notification
.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 133.0
**URL:** https://docs.netskope.com/en/netskope-private-access-release-notes-version-133-0/
**Last Modified:** 2025-12-10T05:07:46+00:00
**Scraped:** 2026-09-03T11:38:48.452445+00:00

Netskope Private Access Release Notes Version 133.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 133.0
Published on: December 10, 2025
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 133.0
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-netskope-private-access-version-133-0/
**Last Modified:** 2026-03-31T00:38:37+00:00
**Scraped:** 2026-09-03T11:38:49.535851+00:00

Netskope Private Access Release Notes Version 133.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 133.0
Published on: December 10, 2025
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 133.0
**URL:** https://docs.netskope.com/en/fixed-issues-in-netskope-private-access-version-133-0/
**Last Modified:** 2026-02-09T23:55:30+00:00
**Scraped:** 2026-09-03T11:38:50.619357+00:00

Netskope Private Access Release Notes Version 133.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 133.0
Published on: December 10, 2025
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues

---
## Netskope Private Access Publisher Release Notes Version 134.0
**URL:** https://docs.netskope.com/en/netskope-private-access-publisher-release-notes-version-134-0/
**Last Modified:** 2026-02-10T03:57:42+00:00
**Scraped:** 2026-09-03T11:39:32.340594+00:00

Netskope Private Access Publisher Release Notes Version 134.0 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 134.0
Published on: February 10, 2025
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues
Known Issues
Deprecated

---
## Netskope Private Access Publisher Release Notes Version 134.0
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-netskope-private-access-version-134-0/
**Last Modified:** 2026-05-18T21:29:54+00:00
**Scraped:** 2026-09-03T11:39:33.427545+00:00

Netskope Private Access Publisher Release Notes Version 134.0 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 134.0
Published on: February 10, 2025
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues
Known Issues
Deprecated

---
## Netskope Private Access Publisher Release Notes Version 134.0
**URL:** https://docs.netskope.com/en/fixed-issues-in-netskope-private-access-version-134-0/
**Last Modified:** 2026-05-18T21:30:16+00:00
**Scraped:** 2026-09-03T11:39:34.509525+00:00

Netskope Private Access Publisher Release Notes Version 134.0 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 134.0
Published on: February 10, 2025
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues
Known Issues
Deprecated

---
## Netskope Private Access Publisher Release Notes Version 134.0
**URL:** https://docs.netskope.com/en/known-issues-in-netskope-private-access-version-134-0/
**Last Modified:** 2026-02-10T18:30:34+00:00
**Scraped:** 2026-09-03T11:39:35.615705+00:00

Netskope Private Access Publisher Release Notes Version 134.0 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 134.0
Published on: February 10, 2025
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues
Known Issues
Deprecated

---
## Netskope Private Access Publisher Release Notes Version 134.0
**URL:** https://docs.netskope.com/en/deprecated-features-in-netskope-private-access-version-134-0/
**Last Modified:** 2026-02-10T03:56:29+00:00
**Scraped:** 2026-09-03T11:39:36.700902+00:00

Netskope Private Access Publisher Release Notes Version 134.0 - Netskope Technical Documentation
Netskope Private Access Publisher Release Notes Version 134.0
Published on: February 10, 2025
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues
Known Issues
Deprecated

---
## Netskope Private Access Release Notes Version 135.0
**URL:** https://docs.netskope.com/en/netskope-private-access-release-notes-version-135-0/
**Last Modified:** 2026-03-11T18:29:07+00:00
**Scraped:** 2026-09-03T11:40:05.369606+00:00

Netskope Private Access Release Notes Version 135.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 135.0
Published on: March 11, 2026
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New

---
## Netskope Private Access Release Notes Version 135.0
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-netskope-private-access-version-135-0/
**Last Modified:** 2026-03-11T18:27:39+00:00
**Scraped:** 2026-09-03T11:40:06.478776+00:00

Netskope Private Access Release Notes Version 135.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 135.0
Published on: March 11, 2026
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New

---
## Netskope Private Access Release Notes Version 136.0
**URL:** https://docs.netskope.com/en/netskope-private-access-release-notes-version-136-0/
**Last Modified:** 2026-04-17T21:57:18+00:00
**Scraped:** 2026-09-03T11:40:40.262295+00:00

Netskope Private Access Release Notes Version 136.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 136.0
Published on: April 17, 2026
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 136.0
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-netskope-private-access-version-136-0/
**Last Modified:** 2026-07-02T20:51:06+00:00
**Scraped:** 2026-09-03T11:40:41.350099+00:00

Netskope Private Access Release Notes Version 136.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 136.0
Published on: April 17, 2026
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 136.0
**URL:** https://docs.netskope.com/en/fixed-issues-in-netskope-private-access-version-136-0/
**Last Modified:** 2026-05-18T21:31:38+00:00
**Scraped:** 2026-09-03T11:40:42.436062+00:00

Netskope Private Access Release Notes Version 136.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 136.0
Published on: April 17, 2026
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 137.0
**URL:** https://docs.netskope.com/en/netskope-private-access-release-notes-version-137-0/
**Last Modified:** 2026-05-14T19:34:44+00:00
**Scraped:** 2026-09-03T11:41:26.308854+00:00

Netskope Private Access Release Notes Version 137.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 137.0
Published on: May 14, 2026
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues
Known Issues

---
## Netskope Private Access Release Notes Version 137.0
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-netskope-private-access-version-137-0/
**Last Modified:** 2026-06-16T00:04:24+00:00
**Scraped:** 2026-09-03T11:41:27.390971+00:00

Netskope Private Access Release Notes Version 137.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 137.0
Published on: May 14, 2026
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues
Known Issues

---
## Netskope Private Access Release Notes Version 137.0
**URL:** https://docs.netskope.com/en/fixed-issues-in-netskope-private-access-version-137-0/
**Last Modified:** 2026-05-14T19:35:17+00:00
**Scraped:** 2026-09-03T11:41:28.473283+00:00

Netskope Private Access Release Notes Version 137.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 137.0
Published on: May 14, 2026
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues
Known Issues

---
## Netskope Private Access Release Notes Version 137.0
**URL:** https://docs.netskope.com/en/known-issues-in-netskope-private-access-version-137-0/
**Last Modified:** 2026-06-01T23:05:14+00:00
**Scraped:** 2026-09-03T11:41:29.560803+00:00

Netskope Private Access Release Notes Version 137.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 137.0
Published on: May 14, 2026
We are excited to announce our release updates! Get the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues
Known Issues

---
## Netskope Private Access Release Notes Version 138.0
**URL:** https://docs.netskope.com/en/netskope-private-access-release-notes-version-138-0/
**Last Modified:** 2026-06-16T02:30:21+00:00
**Scraped:** 2026-09-03T11:41:56.804017+00:00

Netskope Private Access Release Notes Version 138.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 138.0
Published on: June 16, 2026
We are excited to announce our release updates! Here are the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 138.0
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-netskope-private-access-version-138-0/
**Last Modified:** 2026-08-24T19:12:06+00:00
**Scraped:** 2026-09-03T11:41:57.891411+00:00

Netskope Private Access Release Notes Version 138.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 138.0
Published on: June 16, 2026
We are excited to announce our release updates! Here are the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 138.0
**URL:** https://docs.netskope.com/en/fixed-issues-in-netskope-private-access-version-138-0/
**Last Modified:** 2026-06-17T20:26:15+00:00
**Scraped:** 2026-09-03T11:41:58.972790+00:00

Netskope Private Access Release Notes Version 138.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 138.0
Published on: June 16, 2026
We are excited to announce our release updates! Here are the latest features, issues fixed, and other updates in this release.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 139.0
**URL:** https://docs.netskope.com/en/netskope-private-access-release-notes-version-139-0/
**Last Modified:** 2026-08-18T08:29:43+00:00
**Scraped:** 2026-09-03T11:42:26.882366+00:00

Netskope Private Access Release Notes Version 139.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 139.0
Published on: July 16, 2026
We are excited to announce our release updates! Here are the latest features, fixed issues, and other updates in this release.
What's New
Fixed Issues
Known Issues

---
## Netskope Private Access Release Notes Version 139.0
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-netskope-private-access-version-139-0/
**Last Modified:** 2026-07-16T18:40:56+00:00
**Scraped:** 2026-09-03T11:42:27.991213+00:00

Netskope Private Access Release Notes Version 139.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 139.0
Published on: July 16, 2026
We are excited to announce our release updates! Here are the latest features, fixed issues, and other updates in this release.
What's New
Fixed Issues
Known Issues

---
## Netskope Private Access Release Notes Version 139.0
**URL:** https://docs.netskope.com/en/fixed-issues-in-netskope-private-access-version-139-0/
**Last Modified:** 2026-07-16T18:41:10+00:00
**Scraped:** 2026-09-03T11:42:29.099637+00:00

Netskope Private Access Release Notes Version 139.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 139.0
Published on: July 16, 2026
We are excited to announce our release updates! Here are the latest features, fixed issues, and other updates in this release.
What's New
Fixed Issues
Known Issues

---
## Netskope Private Access Release Notes Version 139.0
**URL:** https://docs.netskope.com/en/known-issues-in-netskope-private-access-version-139-0/
**Last Modified:** 2026-07-16T18:41:30+00:00
**Scraped:** 2026-09-03T11:42:30.236515+00:00

Netskope Private Access Release Notes Version 139.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 139.0
Published on: July 16, 2026
We are excited to announce our release updates! Here are the latest features, fixed issues, and other updates in this release.
What's New
Fixed Issues
Known Issues

---
## Netskope Private Access Release Notes Version 140.0
**URL:** https://docs.netskope.com/en/netskope-private-access-release-notes-version-140-0/
**Last Modified:** 2026-08-18T08:49:12+00:00
**Scraped:** 2026-09-03T11:43:07.350223+00:00

Netskope Private Access Release Notes Version 140.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 140.0
Published on: August 18, 2026
We are excited to announce our release updates! Here are the latest features, fixed issues, and other updates in this release.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 140.0
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-netskope-private-access-140-0/
**Last Modified:** 2026-08-25T01:47:51+00:00
**Scraped:** 2026-09-03T11:43:08.457046+00:00

Netskope Private Access Release Notes Version 140.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 140.0
Published on: August 18, 2026
We are excited to announce our release updates! Here are the latest features, fixed issues, and other updates in this release.
What's New
Fixed Issues

---
## Netskope Private Access Release Notes Version 140.0
**URL:** https://docs.netskope.com/en/fixed-issues-in-netskope-private-access-140-0/
**Last Modified:** 2026-08-18T08:53:08+00:00
**Scraped:** 2026-09-03T11:43:09.604652+00:00

Netskope Private Access Release Notes Version 140.0 - Netskope Technical Documentation
Netskope Private Access Release Notes Version 140.0
Published on: August 18, 2026
We are excited to announce our release updates! Here are the latest features, fixed issues, and other updates in this release.
What's New
Fixed Issues
