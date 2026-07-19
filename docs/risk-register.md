# Risk Register

| Risk ID | Category | Risk Description | Affected Feature / Requirement | Severity | Likelihood | Mitigation Action | Owner | GitHub Evidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| R-01 | Privacy | Users may upload building images that accidentally include people or personal information. | FR-15 | Medium | Low | Display a privacy notice and instruct users to upload only building images without personal information. | Member 1 | Issue #6 | Open |
| R-02 | Ethical | AI may incorrectly recognize a building, causing users to receive incorrect campus information. | FR-03, FR-07 | Medium | Medium | Train the AI model with more building images and display a disclaimer when confidence is low. | Member 1 | Issue #6 | Open |
| R-03 | IP | Third-party assets (Bootstrap, Font Awesome, Google Fonts, Google Teachable Machine) may not be properly credited. | FR-16 | Low | Low | Maintain an IP and Third-Party Assets Register and provide appropriate acknowledgements. | Member 2 | Issue #4 | Open |
| R-04 | Security | Unauthorized users may attempt to access the admin management page. | FR-09 | High | Low | Protect the admin page with authentication and restrict editing permissions to administrators. | Member 2 | Issue #5 | Open |
| R-05 | Legal | Campus photos or maps may be used without appropriate permission. | FR-15 | Medium | Low | Use only team-created photos or resources with permission for educational purposes. | Member 1 | Issue #4 | Open |
| R-06 | Data Quality | Building information or opening hours stored in the JSON database may become outdated. | FR-04, FR-09 | Medium | Medium | Allow administrators to regularly review and update the JSON data. | Member 2 | Issue #6 | Open |

## Overall Risk Decision

The project is safe to continue with minor revisions. No critical risks prevent further development of the prototype. Before the final implementation, the team will improve AI recognition accuracy, strengthen administrator authentication, ensure proper attribution of third-party assets, review campus information regularly, and continue following privacy and responsible data handling practices.
