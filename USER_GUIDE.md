# Carigara Disaster Early Warning System — User Guide

## Overview
This guide explains how to use the Carigara Incident Management System from a user perspective.
The system supports three main user types:
- **Admin** — manage incidents, response workflows, and hazard data.
- **Dispatcher** — create and update incidents and support response operations.
- **Viewer** — read-only access to incident reports and public incident dashboard.

The application also includes a superadmin role for user management and system administration.

## Start Page
Open the application at:

```text
http://localhost:8000/
```

The first page is the welcome page. It includes:
- a branded landing screen
- login and register buttons
- a quick summary of system capabilities

If you are already logged in, the welcome page now remains visible and includes a button to go to the dashboard.

## Authentication

### Login
- Click **Login** on the home page.
- Enter your username and password.
- If login succeeds, you can access your role-specific dashboard.

### Register
- Click **Register** on the welcome page.
- This creates a new **public viewer** account.
- Public viewers can only view incident reports, not create or edit incidents.

### Password Management
- Use **Forgot password?** on the login page to reset your password.
- Password reset flows are handled by email templates configured in the system.

## Dashboard and Navigation

### Dashboard
The dashboard shows:
- incident totals and counts by status
- unresolved incident summaries
- priority and alert-level breakdowns
- quick actions for creating new incidents

The main navigation and page flow are:
- Home: `/`
- Login: `/login/`
- Register: `/register/`
- Dashboard: `/incidents/dashboard/`
- Incident create: `/incidents/incident/new/`
- Incident view: `/incidents/incident/<id>/`
- Profile: `/profile/`

## Incident Workflow

### Creating an Incident
- Available to **admin** and **dispatcher** users.
- Go to the incident creation page or use quick action links if shown on the dashboard.
- Fill in incident details such as type, title, description, location, latitude, longitude, priority, and attachments.
- Save the incident.

### Viewing an Incident
- Use the incident list or dashboard to click an incident.
- The incident detail page shows all incident information and attached images.

### Updating Incident Status
- Edit an incident and change its **Status** field.
- When the status changes, the system sends an email notification to:
  - the incident reporter
  - the assigned dispatcher
  - admin users

This notification works for:
- manual incident updates in the web view
- API status updates via `/api/incidents/incidents/<id>/update_status/`
- admin bulk status actions (`Mark selected incidents as CONFIRMED` / `RESOLVED`)

## Email Notifications

### What triggers email
- status changes on incidents.
- admin bulk actions that mark incidents confirmed or resolved.

### Who receives email
- the user who reported the incident
- the dispatcher assigned to the incident
- all admin users in the system

### Developer note
- In development (`DEBUG=True`), emails are printed to the server console.
- In production, configure a real SMTP backend using environment variables.

## User Roles

### Superadmin
- full access to user management and activity logs
- can create and update users
- can see system account usage

### Admin
- manage incidents and hazards
- does not see global user/activity pages unless also superadmin

### Dispatcher
- create incidents
- update incidents they are assigned to or reported

### Viewer
- read-only access to incident reports
- can register for a public viewer account

## User Profile
- Access your profile at `/profile/`
- The profile page shows your username, email, role, phone, and account dates
- Change your password using the password change page after login

## Admin Actions

### Bulk Incident Actions
- In Django admin, select multiple incidents.
- Use bulk actions to mark them **CONFIRMED** or **RESOLVED**.
- This also sends status-change emails to relevant users.

### User management
- Superadmin can create and update users at `/users/`
- This includes account roles and permissions

### Account activity
- Superadmin can review login/logout activity at `/users/activity/`

## Public Viewer Access
- Public viewers can see a read-only incident report table.
- They cannot create incidents or access admin features.
- Public viewers are appropriate for community members who need incident information only.

## Tips
- If you are already logged in, use the dashboard button from the welcome page.
- If an incident is created but no email is sent, check whether the status was changed after creation.
- For immediate alerts, change the incident status rather than just creating the incident.

## Useful Links
- Home: `/`
- Login: `/login/`
- Register: `/register/`
- Dashboard: `/incidents/dashboard/`
- Incident create: `/incidents/incident/new/`
- Profile: `/profile/`
- API docs: `/api/docs/`

## Support
If you need help, open the system logs or inspect browser/network errors.
If the welcome page is not visible, clear cookies or open the site in a private browser window.
