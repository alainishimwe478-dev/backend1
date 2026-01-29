# TODO List for Building FastAPI Backend for AdminDashboard

## Completed Steps
- [x] Update models.py to add Hospital and Claim classes
- [x] Create routes/admin.py with three endpoints: /api/admin/stats, /api/admin/recent-claims, /api/admin/fraud-claims
- [x] Update main.py to import and include admin_router
- [x] Secure admin endpoints with JWT authentication (require admin role)

## Pending Steps
- [x] Run the backend with `uvicorn main:app --reload` (default port 8000)
- [x] Test the endpoints at http://127.0.0.1:8000/docs
- [x] Address port mismatch: Frontend calls localhost:5000, but FastAPI runs on 8000. Options: Change frontend URLs to 8000 or run FastAPI on port 5000 with `uvicorn main:app --reload --port 5000`
