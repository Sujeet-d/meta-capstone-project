==================================================
LITTLE LEMON RESTAURANT API - PEER REVIEW GUIDE
==================================================

1. User Registration & Authentication (Djoser)
   - POST: http://127.0.0.1:8000/auth/users/ (Register a user)
   - POST: http://127.0.0.1:8000/restaurant/api-token-auth/ (Login / Obtain Token)

2. Menu API Endpoints
   - GET / POST: http://127.0.0.1:8000/restaurant/menu/
   - GET / PUT / DELETE: http://127.0.0.1:8000/restaurant/menu/<id>

3. Booking API Endpoints (Requires Token Authentication Header)
   - GET / POST: http://127.0.0.1:8000/restaurant/booking/tables/