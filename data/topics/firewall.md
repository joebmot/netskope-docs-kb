# Netskope Docs — Firewall
_Generated: 2026-06-24 10:30 UTC_
_Pages: 12_

---
## Check Firewall Policy
**URL:** https://docs.netskope.com/en/check-firewall-policy/
**Last Modified:** 2026-03-06T02:17:29+00:00
**Scraped:** 2026-06-24T09:22:46.421523+00:00

Check Firewall Policy
Soon you’ll be installing the Netskope Client (which is used to automatically forward traffic to the Netskope cloud) to user devices, and you must ensure that it is able to communicate to the Netskope Cloud.
Ensure that the following are permitted through both any installed Endpoint firewall software (like Windows Firewall, Crowdstrike, etc.) and any on-premise network firewall (like Palo Alto, Fortinet, etc.):
TCP 443 towards the Netskope IP range:
163.116.128.0/17
,
162.10.0.0/17
TCP 53 & UDP 53 (DNS) towards
dns.google
(
8.8.8.8
and
8.8.4.4
).
Note
Google DNS is used for geolocation purposes to determine the closest Netskope data center to connect the user to.
Important
You should ensure that the Netskope IP range is
bypassed
from any SSL decryption/inspection mechanisms you are running on perimeter security appliances or internal proxy servers.
All connections between the Netskope Client and Netskope cloud are Certificate-Pinned to prevent Man-in-the-Middle attacks, so attempting to inspect this connection will cause it to fail.
In this Topic
Check Firewall Policy

---
## Cloud Firewall Advanced Analytics Events
**URL:** https://docs.netskope.com/en/cloud-firewall-advanced-analytics-events/
**Last Modified:** 2025-08-31T01:50:43+00:00
**Scraped:** 2026-06-24T09:26:18.583935+00:00

Cloud Firewall Advanced Analytics Events - Netskope Knowledge Portal
Cloud Firewall Advanced Analytics Events
Cloud Firewall Events log all traffic that is steered to Netskope through Cloud Firewall.
Note
Your account must be enabled for Cloud Firewall and an additional license is required to use Cloud Firewall Events.
To view Cloud Firewall Events, go to
Advanced Analytics > Explore > Data Collection > Cloud Firewall Events.
To learn more about the dimensions and fields:
Exploring Data in Reports
Use the Cloud Firewall Discovery Dashboard to get started reporting on Cloud Firewall Events. You can filter and sort this information and save the dashboard to your library.
The following table shows the default Cloud Firewall Discovery Dashboard default tiles.
Tile Name
Description
Discovered Users
Total number of discovered users.
Hosts & Ports Discovered
Cloud Firewall policy in use, with host and ports, number of users, number of connections, and total byte traffic.
Policies Accessed
Total number of policies accessed.
Top Blocked Services
Shows the blocked applications (IP Protocol, Destination Port, Destination IP).
Top Users by Total Bytes
Shows the top users by bandwidth consumption, with the “Allow” policy action.
Top Users/Source IP by Blocked Connections
Shows top users/source IP blocked by number of connections.
Total Bandwidth Consumption
Traffic flow by total bytes (GB).
Trend of Total Bandwidth Consumption by Top Users
Shows the top users by bandwidth consumption with the “Allow” policy action.
Trend of Total Bandwidth Consumption by Top Business Units
Shows the top user groups by bandwidth consumption with the “Allow” policy action.
Trend of Total Bandwidth Consumption by Traffic Direction
Shows the flow of byte traffic by policy (uploads and downloads).
Trend of Network Activities
Shows the trend for the following network activities: users, events, and total bytes (GB).
To learn more about dashboards:
Netskope Library
and
Creating Reports (Dashboards)
In this Topic
Cloud Firewall Advanced Analytics Events

---
## Cloud Firewall Network Events and Alerts
**URL:** https://docs.netskope.com/en/cloud-firewall-network-events-and-alerts/
**Last Modified:** 2025-08-31T01:50:42+00:00
**Scraped:** 2026-06-24T09:26:22.978369+00:00

Cloud Firewall Network Events and Alerts - Netskope Knowledge Portal
Cloud Firewall Network Events and Alerts
Network Events log all traffic that is steered to Netskope at the connection level.
To view Network events, go to
Skope IT > Events > Network Events
.
Note
For all traffic except HTTP(s), system logs once when the session is established and logs again when the session closes. For HTTP(s) traffic, system only logs when the session closes.
The default Network Events page table includes:
Time: The day and hour the event occurred
Username: email address of the user that caused the alert
Application: The application specified, if any, in the Real-Time Protection policy
DST Port: User’s destination port
Traffic Type: NSFW which stands for Netskope Firewall (NOTE: Traffic Type is not visible by default. Click the
icon to open the Customize Columns window and add it to the table view).
Policy Name: The name of the Real-Time Protection policy
Action: The action specified in the Real-Time Protection policy
Total Bytes: Total Bytes transferred using the traffic flow (Total Bytes = Bytes Uploaded by User + Bytes Downloaded from Server)
To view detailed information about a network event, click the  icon.
Other page components include:
Refresh Page button: To update the page with the most current information, click the Refresh icon next to the page title.
Date Range list: In the top right corner of the page is a date range filter. Click the toggle and select one of these date ranges.
Application Name search filter: This search field helps you find applications and then filter results. Enter a name and then select from the list.
You can filter a field by null value. Operators like = and != will work for filtering by null.
Add Filter lists: To create a filter, click
+ Add Filter
, select what to include what to find in the search, and then click
Apply
.
Tip
You can choose multiple items for some options. The options with the  icon allows you to search.
The
+ Add Filter
button will allow you to select multiple traffic types.
Query Mode button: Optionally, switch to query mode  and enter a query in the search field. For example, to specify firewall traffic type events, enter the following query.
traffic_type eq NSFW
To change back to the filter view, click
Filter Mode
.
Save Filter button: After adding a filter, you can save it for future searches by clicking Save Filter.
Sort by: Time, Total Bytes, Bytes Uploaded, Bytes Downloaded. This sorts the table columns.
Export button: Click
Export
to get the entire list of network events. First select the columns to export (those displayed, or specify which columns), and the number of rows, then click Export again. Your column and row selections are retained for future exports.
The system sends an email with a link that allows you to download the list in CSV format.
Rows per page list: At the bottom right corner of the page, the Rows per page list allows you to display 10, 20, 30, 50, or 100 rows per page.
Customize Columns
Use the Customize Columns dialog box to specify the information you want to see. Click the gear icon  located at the far right of the table column header row, and then select the columns you want to see.
Source: includes Username, Source Location, Source Region, Source Country
General: includes Application, Traffic Type, Policy Name, Action
Destination: includes Destination Host, Destination Port, IP Protocol, Destination Location, Destination Region, Destination Country
Session: includes Number of Sessions, Total Bytes, Bytes Uploaded, Bytes Downloaded
Click
Restore Defaults
to restore column-related default settings.
Cloud Firewall Alerts
Firewall alerts are logged if traffic is blocked by the explicit firewall rule. Alerts display in the list page. Admins must review and acknowledge the event and take additional action as needed.
To view Network events, go to
Skope IT > Events
.
The page components are similar to the Network Events. However, the main difference is the  button.
To remove an alert from this page, enable the check boxes beside one or more alerts, click
Acknowledge
, and then choose
Selected Alerts
or
All Alerts
. Acknowledging the alerts will remove them from this list.
In this Topic
Cloud Firewall Network Events and Alerts

---
## Configuring Cloud Firewall Steering Exceptions
**URL:** https://docs.netskope.com/en/configuring-cloud-firewall-steering-exceptions/
**Last Modified:** 2026-02-17T18:22:18+00:00
**Scraped:** 2026-06-24T09:27:00.586020+00:00

Configuring Cloud Firewall Steering Exceptions - Netskope Knowledge Portal
Configuring Cloud Firewall Steering Exceptions
Navigate to
Settings > Security Cloud Platform > Traffic Steering > Steering Configuration > Default tenant config > Exceptions
tab to view the Exceptions list page.
Exception configurations are not a single global list for the entire account, they are part of each Steering Configuration workflow. Exceptions are configured by first selecting a steering configuration, and then clicking
Exceptions
, which enables you to specify the traffic you want to bypass the Netskope Cloud.
Steering configuration controls what kind of traffic gets steered to Netskope for real-time deep analysis and what kind of traffic gets bypassed. Admins can configure a set of firewall apps to bypass processing using the Exceptions feature.
When using exceptions, consider these factors:
In order to use this feature, you must first be steering all traffic to Netskope.
Settings > Security Cloud Platform > Steering Configuration
Click into the desired steering configuration and click “Edit”
Under “Cloud, Web, and Firewall” click the drop down and select “All Traffic” and “Bypass exception traffic at: “Client”.
Netskope Client will not steer traffic to the Netskope cloud for any apps in the exception list. However, the Netskope proxy and app-firewall can still receive traffic matching this exception list in the following scenarios:
when traffic is steered to the Netskope cloud through GRE or IPSec tunnels, or,
when the Netskope Client detects an upstream GRE/IPSec tunnel and goes dormant and does not process exceptions, or,
when the steering and exception configuration are updated in the Netskope UI and the new version takes too long to reach the Netskope Client but the Netskope proxy and app-firewall have the new version already.
Creating Application Exceptions
To learn more:
Adding Exceptions
.
Creating DNS Exceptions
To learn more:
Adding Exceptions
.
Note
VMware Fusion forwards all DNS request by NAT due of which DNS exceptions fail. Follow the below steps to use DNS Security as an additional parameter in nat.conf.
Add below given parameter to “/Library/Application Support/VMware Fusion/vmnet8/nat.conf” and restart your Mac device.
[dns]
prohibitHostLookup = 1
Bypassing Network Events
If you bypassed traffic locally on the device, then the traffic won’t be sent to Netskope and logged in Skope IT events. You can only see logs for traffic bypassed on Netskope.
Click the pencil icon to view the Log Bypassed Traffic window. Enable the
Log
radio button and click
Save
.
Navigate to Skope IT > Network Events to view your bypassed applications.
In this Topic
Configuring Cloud Firewall Steering Exceptions

---
## Creating a Firewall App Definition
**URL:** https://docs.netskope.com/en/creating-a-firewall-app-definition/
**Last Modified:** 2025-08-31T01:50:40+00:00
**Scraped:** 2026-06-24T09:27:51.762151+00:00

Creating a Firewall App Definition
If you have the Cloud Firewall license, on the App Definition page, you can create new rules for firewall apps to apply to policies. You can create multiple rules for the same firewall app. For example, if you create an app called “Allow_FTP” with a certain destination IP and protocol, this same app can be reused to add more destination IPs and protocols.
Custom apps that only have traffic-based definition rules won’t have activities detected. You cannot add Firewall apps to steering.
To create a firewall app definition:
Go to
Settings
>
Security Cloud Platform
>
App Definition
.
In the
Cloud & Firewall Apps
tab, click
New App Definition Rule
and then
Firewall App
.
In the
New App Definition Rule: Firewall App
window:
Application
: Choose an existing firewall custom app or create a new one, and then enter a name for the app. A firewall custom app can’t have the same name as a cloud custom app.
Destination IP
: Enter a valid IP address, IP range, FQDN, PQDN, or CIDR netmask separated by commas. If you leave it empty, Netskope sets the destination IP to any. Examples:
Single IP address –
192.168.1.1
,
192.168.1.2
,
2001:0db8:85a3:0000:0000:8a2e:0370:7334
IP address range –
192.168.1.0-192.168.1.255
,
2001:0db8:: - 2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
CIDR netmask –
192.168.1.0/24
,
2001:db8::/32
FQDN –
example.com
,
mail.example.com
PQDN –
mail.example
A Partially Qualified Domain Name (PQDN) relies on the local DNS resolver or search domains to resolve the name to a Fully Qualified Domain Name (FQDN). For instance, if the local domain is set to
example.com
, the PQDN
mail.example
could resolve to
mail.example.com
.
Protocol
: Choose the protocol for the firewall app. For TCP, UDP, and TCP/UDP, you can enter:
A specific port: 22
A specific port range: 1024-2048
A combination of ports and port ranges: 22,80,443,1024-2048
ICMP
doesn’t require port configuration. A TCP flow times out after 5 minutes of idle time. Netskope recommends you use a keepalive for TCP-based protocols that might leverage longer idle sessions such as SSH, FTP, etc.
Click
Save
.
Following is the rule order of custom app definitions and policies:
Firewall Apps – Netskope picks the app that matches first in the policies, i.e. the app matches by the policy ordered list.
Cloud Apps – Netskope finds the most specific application first then matches by the policy ordered list.
If the app matches both Cloud and Firewall apps as described above (i.e. there is overlap), Netskope uses policy ordering to determine a priority.
In this Topic
Creating a Firewall App Definition

---
## Netskope Client Support in Cloud Firewall
**URL:** https://docs.netskope.com/en/netskope-client-support-in-cloud-firewall/
**Last Modified:** 2026-05-12T18:04:01+00:00
**Scraped:** 2026-06-24T09:31:09.628297+00:00

Netskope Client Support in Cloud Firewall - Netskope Knowledge Portal
Netskope Client Support in Cloud Firewall
Netskope client is an agent-based deployment method where a lightweight non-intrusive agent is installed on the endpoint. The Netskope client provides the most comprehensive coverage as they can be installed on managed devices to provide visibility and policy enforcement for devices that are both on-premises and remote (off network).
The Netskope client steers the traffic from the users’ device to the Netskope cloud based on certain rules and policies. HTTP(S) and non-HTTP(S) traffic is sent to Netskope gateway and based on traffic type, HTTP(S) traffic is forwarded to Netskope Proxy and non-HTTP(S) traffic is forwarded to Netskope Cloud Firewall. Netskope cloud performs policy enforcement, and the activity is displayed on the Netskope console in the cloud.
This article focuses on steering the non-HTTP(S) traffic to the Netskope Cloud Firewall.
A typical Netskope Cloud Firewall network diagram (with Netskope client) is as follows:
Netskope Client reads the DNS query before sending it to Cloud Firewall in order to apply possible DNS Steering Bypasses based on the requested record. If the Netskope client cannot read the actual query inside the DNS packet (for instance if the DNS query is DNScrypt on UDP/TCP 53), the query is steered inside the tunnel without the possibility to perform DNS Steering Bypasses.
Netskope Client logs TCP-based traffic as Cloud Firewall tunneling entries at the
info
log level (the default) and the UDP-based traffic as Cloud Firewall tunneling entries at the
debug
log level.
Netskope Client (with Cloud Firewall) Supported Operating System
Netskope client (with cloud firewall) supports the following operating systems:
Windows 10 or later
Windows Server 2016 or later
macOS Big Sur or later
iOS 15 or later
If you have a older version of Windows or macOS, refer
Netskope Client Dynamic Steering, Fall Back, and Fail Close Behavior
.
Configure Netskope Client to Steer Non-HTTP(S) Traffic
To configure Netskope client to steer non-HTTP(S) traffic to Netskope Cloud Firewall, follow the steps below:
Set Traffic Steering to All Traffic
Netskope client needs to steer HTTP(S) as well as non-HTTP(S) traffic to the Netskope cloud. To set the traffic steering option, follow the steps below:
Log in to the Netskope tenant UI.
Navigate to
Settings > Security Cloud Platform > Traffic Steering > Steering Configuration
.
Click the
Default tenant config
entry.
On the top-right, click
EDIT
and set the
Traffic Steering
option to
All Traffic
.
Click
Save
.
Create a Firewall App and Real-time Protection Policy
Then, you can create an App Definition, followed by a Real-time Protection policy. Click the following links to go to the respective procedure:
Creating a Firewall App Definition
Real-time Protection Policies
Configure Steering Exceptions
If you have a requirement for the Netskope client to bypass certain non-HTTP(S) applications, follow the steps below:
Note
Ensure that you have already created a firewall application from the
Settings > Security Cloud Platform > Traffic Steering > App Definition
page.
If you have created a firewall application using wildcards (for example, *.xyz.com), the Netskope client bypasses the subdomain entries only (i.e., mail.xyz.com, play.xyz.com), the root domain (i.e., xyz.com) continues to get steered to the Netskope gateway. To avoid this, ensure that you explicitly add the root domain in the
App Definition
page and include this application in the exception list.
Log in to the Netskope tenant UI.
Navigate to
Settings > Security Cloud Platform > Traffic Steering > Steering Configuration
.
Click the
Default tenant config
entry.
Under the
Exceptions
tab, click the
New Exception
drop-down list and select
Application
.
Select the firewall application you created in the
App Definition
page and click
Add
.
When the Netskope client is in “All Traffic” mode or cloud firewall is enabled, the following traffic is bypassed by default:
DNS IPv4 ( If the
Steer DNS traffic
option is not selected)
DNS IPV6
Non-HTTP(S) IPv6
Netskope client for macOS in Cloud Firewall mode captures only TCP and UDP traffic. It cannot intercept protocols like ICMP or others that are not based on TCP/UDP.
Note
Netskope client blocks inbound TCP connections from sources that do not fall under the steering exceptions. For example, enabling cloud firewall client on a Windows virtual machine in Amazon Web Services loses Remote Desktop Protocol (RDP) connectivity from the internet. To have seamless connectivity, ensure that such inbound TCP connections are defined under the firewall steering exceptions list.
Deploy the Netskope Client
Documentation on various Netskope client deployment options can be found
here
.
In macOS Ventura or prior versions of macOS, FTP upload fails while using applications like FileZilla. While using FileZilla to upload large files (1G size) through Netskope tunnel, the file upload fails if the upload takes too long and the FTP control channel times out. This large file upload issue can occur even without the Netskope Client (Netskope client is uninstalled).
As a workaround, you can do the following:
1. Enable the
enableMacPerformance
flag on the tenant that was introduced in the Client release 96.
2. Using alternate FTP applications like Cyberduck, MacOS FTP Client [ftp (GNU inetutils)] to perform file uploads.
Netskope Client Dynamic Steering, Fall Back, and Fail Close Behavior
This document outlines the various traffic steering types in the Netskope Client and how dynamic steering, fallback, and fail-close behaviors are managed, particularly differentiating based on the enablement of Flexible Dynamic Steering.
Event Management
Flows managed by NSproxy generate
Transaction Events
while flows managed by Cloud Firewall will generate
Network Events
.
Consider the following context:
With HTTP-AD
disabled
, traffic to port 80 or 443 are sent to NSproxy directly.
Other traffic for ports in
Steering Configuration
>
Non-Standard Ports
is also sent to NSproxy with the selected domain and port combination.
This traffic was destined to 443 and it was sent to nsproxy.
NSproxy respects cloud firewall policy as well.
If CFW policy allows port 80, policy evaluation is stopped and the final verdict is
allow
.
If CFW policy is disabled, the proxy continues evaluating the next policy and hits
block
.
Traffic Steering Types
A quick definition of the various traffic steering types in Netskope Client:
Cloud Apps Only:
Steers only selected applications to the Netskope gateway for deep analysis.
Web Traffic:
Steers all HTTP(S) traffic (typically on port 80 & 443) to the Netskope gateway for deep analysis.
All Traffic:
Steers all HTTP(S) and non-HTTP(S) traffic to the Netskope gateway for deep analysis.
None (New with Flexible Dynamic Steering):
The Netskope Client does not establish a tunnel or steer any traffic.
Dynamic Steering Behavior Based on Flexible Dynamic Steering Enablement
The Netskope Client’s dynamic steering allows traffic mode changes based on the endpoint’s location (on-premises or remote). The specific behavior depends on whether “Flexible Dynamic Steering” is enabled in your Netskope tenant (available from Client version 112.0.0 onwards).
1. When Flexible Dynamic Steering is NOT Enabled (Legacy Behavior)
For tenants or clients where Flexible Dynamic Steering has not been enabled (or for older Client versions/operating systems that do not support it), the dynamic steering behavior is as follows:
Dynamic steering based on location:
Netskope Client traffic steering type automatically changes to
“Cloud Apps Only”
when the endpoint is detected as
on-premises
.
Netskope Client traffic steering type automatically changes to
“All Traffic”
when the endpoint is detected as
remote (off-premises)
.
2. When Flexible Dynamic Steering IS Enabled (Enhanced Behavior)
With Flexible Dynamic Steering enabled (contact Netskope Support for existing tenants, automatically enabled for new tenants), administrators gain granular control over steering modes for both on-premises and off-premises scenarios. This allows for customized policies beyond the fixed “Cloud Apps Only” / “All Traffic” paradigm.
Configurable Dynamic Steering based on location:
For
On-Premise
scenarios, administrators can select the desired steering mode from:
Cloud Apps Only
Web Traffic
All Traffic
None
(Client does not steer traffic)
For
Off-Premise
(remote) scenarios, administrators can select the desired steering mode from:
Cloud Apps Only
Web Traffic
All Traffic
None
(Client does not steer traffic)
This enhanced flexibility allows organizations to define precise steering policies for different network environments.
Netskope Client Fallback Behavior
The Netskope Client is designed to gracefully handle situations where the ideal steering configuration cannot be maintained. In these scenarios, the client may fall back to a “Web Traffic” steering type:
Netskope Client falls back to
“Web Traffic”
steering type when the Netskope gateway is not cloud firewall-ready.
Netskope Client falls back to
“Web Traffic”
steering type on Windows 7, 8, and 8.1 operating systems.
Netskope Client falls back to
“Web Traffic”
steering type on macOS Catalina or earlier operating systems.
Older versions of Netskope Client fall back to
“Web Traffic”
steering type when Cloud Firewall is enabled on the Netskope tenant.
Netskope Client Fail Close Behavior
In “Fail Closed” mode, the Netskope Client prioritizes security by blocking traffic when a secure connection to the Netskope Cloud cannot be established or maintained for steered traffic.
Netskope Client drops both HTTP(S) and non-HTTP(S) steered traffic in “Fail Closed” mode.
Netskope Client bypasses configured exceptions in “Fail Closed” mode, allowing essential traffic to continue.
Netskope Client does not drop ICMP traffic in “Fail Closed” mode.
Connected Netskope Client Status
Once the Netskope client is connected to the Netskope gateway, the client configuration window looks like the image below. Notice the
Traffic Steering Type
is set to
All Traffic
. It means that the cloud firewall mode is enabled and HTTP(S) & non-HTTP(S) traffic are steered to the Netskope gateway.
In this Topic
Netskope Client Support in Cloud Firewall

---
## Creating a Firewall App Definition
**URL:** https://docs.netskope.com/en/creating-a-firewall-app-definition-449298/
**Last Modified:** 2025-09-16T06:08:33+00:00
**Scraped:** 2026-06-24T09:35:47.136756+00:00

Creating a Firewall App Definition - Netskope Knowledge Portal
Creating a Firewall App Definition
If you have the Cloud Firewall license, on the App Definition page, you can create new rules for firewall apps to apply to policies. You can create multiple rules for the same firewall app. For example, if you create an app called “Allow_FTP” with a certain destination IP and protocol, this same app can be reused to add more destination IPs and protocols.
Note
Custom apps that only have traffic-based definition rules won’t have activities detected. You cannot add Firewall apps to steering.
To create a firewall app definition:
Go to
Settings
>
Security Cloud Platform
>
App Definition
.
In the
Cloud & Firewall Apps
tab, click
New App Definition Rule
and then
Firewall App
.
In the
New App Definition Rule: Firewall App
window:
Application
: Choose an existing firewall custom app or create a new one, and then enter a name for the app. A firewall custom app can’t have the same name as a cloud custom app.
Destination IP
: Enter a valid IP address, IP range, FQDN, PQDN, or CIDR netmask separated by commas. If you leave it empty, Netskope sets the destination IP to any.
Protocol
: Choose the protocol for the firewall app. For
TCP
,
UDP
, and
TCP/UDP
, you can enter:
A specific port:
22
A specific port range:
1024-2048
A combination of ports and port ranges:
22,80,443,1024-2048
ICMP
doesn’t require port configuration. A TCP flow times out after 5 minutes of idle time. Netskope recommends you use a keepalive for TCP-based protocols that might leverage longer idle sessions such as SSH, FTP, etc.
Click
Save
.
Following is the rule order of custom app definitions and policies:
Firewall Apps – Netskope picks the app that matches first in the policies, i.e. the app matches by the policy ordered list.
Cloud Apps – Netskope finds the most specific application first then matches by the policy ordered list.
If the app matches both Cloud and Firewall apps as described above (i.e. there is overlap), Netskope uses policy ordering to determine a priority.
In this Topic
Creating a Firewall App Definition

---
## Firewall Settings for DSPM-Hosted Instances
**URL:** https://docs.netskope.com/en/firewall-settings-for-netskope-dspm-hosted-instances/
**Last Modified:** 2026-06-18T22:14:05+00:00
**Scraped:** 2026-06-24T09:53:12.448001+00:00

Firewall Settings for DSPM-Hosted Instances - Netskope Knowledge Portal
Firewall Settings for DSPM-Hosted Instances
Overview
Because the DSPM (also known as
Netskope One DSPM
) application is hosted and managed by Netskope (instead of being self-hosted), you may need to update your firewall/security group settings in order for Netskope DSPM to connect to your Data Stores.
Important Egress Requirements:
The specific firewall configurations you need depend on your deployment use case:
–
For Direct Connections (no sidecar):
Apply the rules in the
DSPM Application Egress
section.
–
For
Single Appliance
Deployments:
Apply the rules in the
DSPM Application Egress
,
Sidecar Egress and Ports
, and
DLP Service Egress
sections. All three apply to the same host.
–
For
Distributed Deployments
(separate sidecars + DLP appliance):
Apply the rules in the
Sidecar Egress and Ports
and
DLP Service Egress
sections to their respective hosts.
DSPM Application Egress
All Data Store scans will originate from these IP addresses, so you need to whitelist them:
This list has been updated to include new public CIDR blocks from Netskope’s AWS accounts. If you use whitelisting, please add these new ranges to ensure uninterrupted connectivity.
IP Address
CIDR by Home POP
35.86.53.159
44.226.200.72
44.236.251.30
44.243.172.80
52.27.197.60
52.27.67.30
52.39.117.251
52.39.99.174
52.40.249.64
52.43.227.202
54.189.99.166
Home POP
CIDR
SJC1
18.98.10.112/28
SJC2
18.98.10.112/28
SV5
18.98.10.112/28
DFW3
18.98.10.112/28
AM2
18.96.33.16/28
FR4
18.96.33.16/28
FRA2
18.96.33.16/28
ZUR2
18.98.224.160/28
LON3
18.98.162.192/28
SIN2
18.99.40.96/28
MEL2
18.98.196.32/28
If you need to identify your home POP, reach out to your account manager.
Sidecar Egress and Ports
If you are using sidecars to connect with your Data Stores, you may need to update your firewall/security group settings in order to provide outbound egress for sidecars to communicate with DSPM.
Additionally, in the distributed deployment model, the sidecar must be able to communicate with the
DLP appliance
via
HTTPS (port 443)
. In the Single Appliance model, this communication happens locally on the same host.
For more information, please visit any of our sidecar installation articles in the
Netskope DSPM Deployment Guides
.
DLP Service Egress
The
DLP appliance
requires its own outbound egress to the internet. This connectivity is necessary for the appliance to validate its license and download configurations.
In this Topic
Firewall Settings for DSPM-Hosted Instances

---
## CCI Cloud Firewall Apps
**URL:** https://docs.netskope.com/en/cci-cloud-firewall-apps/
**Last Modified:** 2026-06-19T16:05:45+00:00
**Scraped:** 2026-06-24T09:54:18.240202+00:00

CCI Cloud Firewall Apps - Netskope Knowledge Portal
CCI Cloud Firewall Apps
Admins can look up Cloud Firewall apps and identify if the app is a firewall only app (L3/L4) or Hybrid app (L3/L4 and L7). This page is dynamic and apps are continually added, removed, and updated.
Users can filter by CCL, app type, or search by app name.
In this Topic
CCI Cloud Firewall Apps

---
## Windows Defender Firewall
**URL:** https://docs.netskope.com/en/windows-defender-firewall/
**Last Modified:** 2026-06-08T17:01:07+00:00
**Scraped:** 2026-06-24T10:06:55.075475+00:00

Windows Defender Firewall - Netskope Knowledge Portal
Windows Defender Firewall
Windows Defender firewall is a stateful host firewall that monitors incoming and outgoing traffic in a device using rules and policies. This document contains the best practices required in Windows Defender Firewall and Netskope Client to ensure smooth interoperability.
Environment
This document was created using the following components:
Netskope Client: 138.0.0
OS: Windows 10, Windows 11, Windows Server 2016, Windows Server 2019, and Windows Server 2022
Interoperability Configuration Requirements
Specific configurations in the Windows Defender firewall ensure processes or traffic from either of the applications are not blocked or directed to the Netskope Cloud.
Configurations In Windows Defender Firewall
The administrators mostly configure Windows Defender firewall in:
Domain environment: This includes configuring rules for all devices in that domain  automatically using Group Policy.
Non-domain environment: This includes configuring firewall policies for non-domain joined devices using tools such as Microsoft Intune, BMC, and so on.
Best Practices:
The administrators can consider certain best practices while configuring the Windows Defender firewall to optimize the security of the devices. To learn more, view
Best Practices
.
Configure GPO In Windows Defender
To open a GPO to Windows Firewall with Advanced Security:
Open the
Group Policy Management
console.
In the navigation pane, expand
Forest (YourForestName)
>
Domains (YourDomainName)
>
Group Policy Objects
.
In the navigation pane of the
Group Policy Management Editor
, navigate to
Computer Configuration
>
Policies
>
Windows Settings
>
Security Settings
>
Windows Firewall with Advanced Security
>
Windows Firewall with Advanced Security
.
Set the firewall to be enabled and click
Windows Firewall Properties
.
Set the following options for Domain Profile, Private Profile, and Public Profile:
Firewall State to On.
Inbound Connections to Block (Default)
Outbound Connections to Allow (Default)
Click
OK
.
Configure Firewall Rules
Go to
Computer Configuration
>
Policies
>
Windows Settings
>
Security Settings
>
Windows Firewall with Advanced Security
>
Windows Firewall with Advanced Security.
Click
Outbound Rules
>
New Rule
.
In the
New Outbound Rule Wizard
window, perform the following:
Rule Type: Select the rule to create.
Protocol and Ports: Select the port the rule applies to.
Action: Select the action to perform when a connection matches the specified conditions.
Profile: Select the applicable profiles where you need to apply the rules.
Name: Enter a name to identify the rule.
After providing all outbound rules, you can see the new rule in the Group Policy Management console.
Validate Firewall Rules
Apply GPO to a computer OU, and view the result on the client firewall configuration or use the command
gpupdate /force
to manually refresh the policy and publish it to the client.
Make sure to install and run the NS Client with Cloud Firewall mode.
On the client machine which is already domain joined, open the RDP application and access the resource. RDP application must be restricted and it should not be steered through NSProxy.
Verifying Interoperability
Netskope Client Features
Refer to the list of
validated use cases
to verify Client operations.
In this Topic
Windows Defender Firewall

---
## Mac Native Firewall
**URL:** https://docs.netskope.com/en/mac-native-firewall/
**Last Modified:** 2026-06-08T17:30:53+00:00
**Scraped:** 2026-06-24T10:07:12.898588+00:00

Mac Native Firewall - Netskope Knowledge Portal
Mac Native Firewall
Apple devices running macOS have built in firewall mechanisms to allow or block incoming or outgoing traffic. Various MDM tools allow deploying configuration policies that can enable or disable firewalls and also deploy firewall rules. This document lists the configuration requirements to ensure Netskope Client and Mac Native Firewall operate smoothly.
Environment
This document was created using the following components:
Netskope Client: 138.0.0
OS: macOS
Interoperability Configuration Requirements
Netskope recommends the following configurations to ensure that Netskope Client can steer traffic directly to Netskope cloud.
Configuring Mac Native Firewall
When configuring policies for Client deployment, ensure that you add options in your MDM tool to enable firewall and open ports 80 and 443.
To deploy Netskope Client in a Virtual Machine (VM), ensure that the Client in the host machine is disabled.
Enable Firewall
The following references can  provide MDM specific configuration guidelines to enable or disable firewalls in a macOS device:
JAMF Pro
Omnissa Workspace One
MS Intune / Endpoint Manager
Verifying Interoperability
Netskope Client
Refer to the list of
validated use cases
that you can use to verify Client operations.
Mac Firewall
Netskope Client is able to bypass exception and tunnel traffic as specified in the steering configuration.
To validate Mac Firewall, enable firewall on your macOS machine from
System Settings
>
Network
>
Firewall
.
After enabling the firewall, no traffic is allowed and gets blocked. Perform the following steps to block port 443:
Open /etc/pf.conf using vim editor.
Add the following rule at the end of pf.conf file – to block 443 port:
block in proto tcp from any to any port 443
block out proto tcp from any to any port 443
Run below command to enable filter
sudo pfctl -e -f /etc/pf.conf
The rule to block is now set and blocks any website traffic.
tail -f /Library/Logs/Netskope/nsdebuglog.log
In this Topic
Mac Native Firewall

---
## Netskope Cloud Firewall
**URL:** https://docs.netskope.com/en/netskope-cloud-firewall/
**Last Modified:** 2026-01-12T22:43:34+00:00
**Scraped:** 2026-06-24T10:07:38.704569+00:00

Netskope Cloud Firewall - Netskope Knowledge Portal
Netskope Cloud Firewall
Note
This document guides you to configure the Netskope Cloud Firewall. The Netskope Cloud Firewall controls your organizations’ outbound non-HTTP(S) traffic. However, if you intend to manage the HTTP(S) traffic (on port 80/443 and non standard ports), you can refer to the Netskope Secure Web Gateway and Netskope Cloud Access Security Broker documentation.
Netskope Cloud Firewall provides centralized management, visibility, and consistent policies for distributed offices and roaming users. Also, advanced security and access controls without the cost, complexity, and performance limitations of traditional firewall appliances. Netskope also provides integrated cloud hosted firewall capabilities that allow granular control over your organizations’ outbound non-HTTP(S) traffic viz., TCP, UDP, and ICMP traffic.
Netskope Cloud Firewall provides network security on outbound traffic across all ports and protocols for users and offices. Cloud Firewall policy controls include 5-tuple (source and destination addresses and ports with protocol), plus user-IDs and group-IDs, fully qualified domains and wildcards as destinations, an application layer gateway for FTP, and firewall event logging.
With Netskope Cloud Firewall, you can apply an allow/block security policy based on source and destination IP address, destination ports, protocols, and users.
Netskope Cloud Firewall Key Benefits and Capabilities
Firewall Policy Controls: Includes 5-tuple (source / destination address and port, protocol), user-IDs and group-IDs, FQDNs and wildcards for egress firewall policy settings.
FTP Application Layer Gateway: Enables seamless use of FTP through cloud edge network address translation services.
Firewall Event Logging: Full logging of all desired cloud firewall events (TCP,UDP, and ICMP), available for export.
Integrated SASE Architecture: Netskope Security Cloud integrates cloud firewall with Secured Web Gateway (SWG), Cloud Access Security Broker (CASB), and Zero Trust Network Access (ZTNA) solutions for users and offices, to provide protection to all ports and protocols. Secure remote users and branch offices with Firewall-as-a-Service (FWaaS) using one console, one policy engine, and one platform.
Lower Cost of Operation: Reduce appliance expenses and maintenance,dependency on endpoint firewalls, and administration efforts with multiple consoles.
Protect Users: Provides network security for outbound traffic on all port sand protocols for safe direct to internet access with the Netskope client on managed devices. Cloud firewall filters egress traffic of managed users covering all ports and protocols, plus FQDNs and wildcards as destinations, an FTP ALG, and with full logging.
Secure Office: Provides network security for all outbound ports and protocols for safe direct to internet access via GRE and IPSec tunnels for any user or device. SD-WAN compatible, cloud firewall supports IPSec and GRE tunnels from offices to the Netskope Security Cloud to filter egress traffic.
DNS Security
Netskope enables you to steer non-HTTP(S) traffic using various methods. The following sections describe the various configuration steps.
Real-time Protection Policies for Cloud Firewall
SOCKS5 Proxy
Configure a GRE Tunnel
Configure an IPSec Tunnel
Network Location
Creating a Firewall App Definition
GRE & IPSec Tunnel Gateway – HTTP(S) Non-Standard Port Support
Configuring Cloud Firewall Steering Exceptions
Netskope Client Support in Cloud Firewall
Cloud Firewall Network Events and Alerts
Cloud Firewall Advanced Analytics Events
Bandwidth Control
SSL Decryption
DNS Security
Best Practices
If you have Explicit Proxy over Tunnel (EPoT) configured, and intend to procure Cloud Firewall license , you
must
adhere to following EPoT guideline prior to Cloud Firewall activation:
1. Use EPoT with port 80 (Recommended by Netskope)
2. If port EPoT has to be used with port 8080 for unavoidable reasons, then you must also define port 8080 in your
Steering Configuration
under
Non-Standard Ports
.
Not following above guidelines would result in traffic loss for EPoT after activation of Cloud Firewall.
Please refer to
/en/explicit-proxy-over-ipsec-and-gre-tunnels#general-guidelines
for more details.
When implementing Cloud Firewall there are a series of general best practices that should be followed. This list contains the best practices that should be followed when implementing Cloud Firewall in the majority of use cases, but it shouldn’t be considered as an exhaustive list as some best practices may depend on the environment, use cases, implementation.
When implementing Cloud Firewall the following are the most general best practices:
Choose the Default Non-Web Policy behavior according to your organization’s security posture.
By default, the Default Non-Web Policy (last resort) blocks all non-web traffic.
Although this default behavior is consistent with general Firewall hierarchies and best practices, it is possible to change the behavior of the Default Non-Web Policy to allow all non-web traffic as a last resort. There are valid use cases for doing so (for testing purposes, for discovery purposes, for a more “relaxed” non-web security posture when it comes to Internet traffic).
Depending on how the Default Non-Web Traffic Policy has been configured, keep in mind that:
If it has been configured to block all non-web traffic, specific Policies that allow the sanctioned traffic must be put in place
If it has been configured to allow all non-web traffic, specific Policies that block the unsanctioned traffic must be put in place
When configuring CFW in the presence of Tunnels, it’s extremely important to:
Correctly define what non-web traffic should be sent to Netskope via Policy Based Routing
Correctly define what are the expected “Custom Web Ports” sent to Netskope and configure them under the Default Steering Configuration. This will ensure that well-known and expected Web traffic sent to non-standard ports (e.g. 8080) will be managed by CASB/SWG which will also apply FW policies instead of CFW.
Since steering CFW traffic using NSClient, not unlike SWG traffic, relies on the ability to filter clear-text DNS queries and associated requested FQDNs to destination IPs to correctly associate the destination FQDN to the outbound TCP/UDP traffic, ensure that:
DNS over HTTPS (DoH) is blocked by the appropriate Policy in the tenant
DNS over TLS (DoT) is blocked by a Custom Firewall Application for port TCP 853 in the tenant
DNS over Quic (DoQ) is blocked by a Custom Firewall Application for port UDP 443 and UDP 853 in the tenant
Configure all the Policies containing L3/4 Custom Firewall Applications above any Policy that contains a L7 Predefined Application. This is to guarantee that the Policies for L3/4 Custom firewall Applications will be triggered at the first packet.
Conversely, configure all the Policies for L7 Predefined Applications below any Policy that contains a L3/4 Custom Firewall Application.
There can be exceptions where one may want to place a Policy containing a L3/4 Custom Firewall Application below a Policy containing a L7 Predefined application, depending on the use case, but those use cases are niche use cases, and in that case one must keep in mind that the Policy containing the L3/4 Custom Firewall Application below any given Policy containing a L7 Predefined Application will trigger and be enforced only after DPI has completed or aborted the inspection of the L7 protocol.
Never mix L3/4 Custom Firewall Applications and L7 Predefined Applications inside the same Policy, for the reasons above, unless the admins have a specific reason for doing so.
Cloud Firewall Policies that act on Web ports/traffic must be placed accordingly to the overall CASB/SWG Policy hierarchy. For instance:
Policies that contain L3/4 Custom Firewall Applications that apply to web ports 80/443 blocking the traffic, would prevent any CASB/SWG traffic if placed above any CASB/SWG Policy
Policies for Hybrid Applications (such as Teams) that apply to both CFW and CASB/SWG allowing the traffic, would prevent any further CASB/SWG Activity/Instance/Threat Protection/DLP policy that is placed below. Hybrid Application Policies must be placed generally at the bottom
In this Topic
Netskope Cloud Firewall
