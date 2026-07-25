# Prototype Testing Notes

## Test Environment
- **Prototype link or folder:** prototype/(frontend.html, admin.html, app.py)
- **Browser/device used:** Google Chrome (Desktop), Microsoft Edge
- **Tester role:** Student and Administrator
- **Test date:** 25 July 2026

---

## Main Test Cases

| Test ID | User Flow / Feature | Steps to Test | Expected Result | Actual Result | Status | Issue Found | Fix / Next Action |
|---|---|---|---|---|---|---|---|
| T-01 | Open Homepage | Open `frontend.html` | Homepage displays project title, navigation menu, chatbot, and campus services | Homepage loaded successfully | ✅ Pass | None | Continue improving UI design |
| T-02 | AI Image Recognition | Upload a campus building image through the chatbot | Google Teachable Machine identifies the building and displays related information | Building information displayed correctly | ✅ Pass | Some similar buildings are occasionally misclassified | Retrain the AI model with additional building images |
| T-03 | View Campus Directory | Open the Directory page | Campus buildings and information are displayed from `database.json` | Building list displayed successfully | ✅ Pass | Some buildings need additional information | Expand the campus database |
| T-04 | Search Buildings | Enter a building name in the search bar | Matching buildings are displayed | Search returned correct results | 🟡 Partial | Category and faculty filters are unavailable | Add advanced filtering options |
| T-05 | View Building Details | Select a building from the directory | Building description, facilities, and floor map are displayed | Building details displayed correctly | ✅ Pass | Some floor maps are missing | Upload additional floor maps |
| T-06 | Admin Building Management | Open `admin.html` and edit building information | Administrator can update building information successfully | Edit function works correctly | 🟡 Partial | Add/Delete functions are not yet implemented | Complete CRUD functionality |
| T-07 | Dashboard and Metrics | Open Dashboard page | Dashboard displays project statistics and startup metrics | Dashboard displays basic statistics | 🟡 Partial | Additional startup metrics are required | Add AI recognition statistics and usage analytics |

---

## Summary of Issues

- Google Teachable Machine occasionally misclassifies buildings with similar appearances.
- Search currently supports keyword search only and does not include category or faculty filters.
- The Admin panel supports editing but still requires complete Add and Delete functions.
- The Dashboard currently displays basic information and should include more startup metrics.
- Some building records in the database require more detailed descriptions, facilities, and floor maps.

---

## Improvements Completed During Lab 11

- Improved Homepage layout and navigation.
- Enhanced Google Teachable Machine integration for image recognition.
- Expanded the campus building database (`database.json`).
- Improved the Campus Directory user interface.
- Enhanced responsive design for desktop and mobile devices.
- Updated Lab 11 documentation, startup metrics, README, and feature implementation status.

### GitHub Commit References

- `docs: update Lab 11 feature implementation status`
- `docs: add Lab 11 startup product metrics`
- `docs: add Lab 11 prototype testing notes`
- `docs: update Lab 11 weekly logbook`
- `docs: update README for Lab 11 Sprint 2`
