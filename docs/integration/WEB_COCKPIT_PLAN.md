# FAZZ-4 Web Cockpit - Backend Integration Plan

**Web Application**: https://fazz4webb1.netlify.app  
**Backend System**: fazz4-system (Mac M2)  
**Integration Type**: Real-time Data Feed  
**DOI**: 10.5281/zenodo.18183914

---

## 🎯 Integration Architecture

### Current State

```
┌─────────────────────────────┐
│   Netlify Web Frontend      │
│   (Static Dashboard)        │
│   - Termal Hasat Display    │
│   - Ontolojik Refleks       │
│   - Ulusal Bilanço          │
└─────────────────────────────┘
              │
              │ (Currently Static)
              ▼
     No Backend Connection
```

### Target State (Integrated)

```
┌─────────────────────────────┐
│   Netlify Web Frontend      │
│   (fazz4webb1.netlify.app)  │
└──────────────┬──────────────┘
               │
               │ WebSocket/REST
               │
┌──────────────▼──────────────┐
│   FAZZ-4 Backend API        │
│   (Mac M2 - FastAPI)        │
│                             │
│   src/interfaces/api/       │
│   └── cockpit_routes.py     │
└──────────────┬──────────────┘
               │
               │
┌──────────────▼──────────────┐
│   FAZZ-4 Protocol Engine    │
│   (src/core/)               │
│                             │
│   - Termal Hasat Processor  │
│   - Ontolojik Refleks       │
│   - Bilanço Calculator      │
└─────────────────────────────┘
```

---

## 🚀 Implementation Steps

### Phase 1: Backend API Endpoints

Create REST API endpoints to feed real-time data to the web cockpit.

**File**: `src/interfaces/api/routes/cockpit.py`

```python
from fastapi import APIRouter, WebSocket
from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any

router = APIRouter(prefix="/api/v1/cockpit", tags=["cockpit"])

# Data Models
class ThermalHarvestData(BaseModel):
    """Termal hasat verileri"""
    motor_temperature_celsius: float
    electron_order_percent: float
    gaia_autonomous_power_days: float
    timestamp: datetime

class OntologicalReflexData(BaseModel):
    """Ontolojik refleks verileri"""
    shock_wave_detected: bool
    status: str  # "STABLE", "UNSTABLE", "CRITICAL"
    reflex_time_seconds: float
    fuel_saved_kg: float
    timestamp: datetime

class NationalBalanceData(BaseModel):
    """Ulusal hasat bilançosu"""
    aircraft_count: int
    fund_usd: float
    co2_prevented_tons: float
    timestamp: datetime

class CockpitDashboard(BaseModel):
    """Tam cockpit dashboard verisi"""
    thermal_harvest: ThermalHarvestData
    ontological_reflex: OntologicalReflexData
    national_balance: NationalBalanceData
    alignment: str  # "L = C.T"
    doi: str

# Endpoints
@router.get("/dashboard", response_model=CockpitDashboard)
async def get_dashboard() -> CockpitDashboard:
    """
    Ana dashboard verilerini döndür.
    Frontend her 1 saniyede bir bu endpoint'i çağırır.
    """
    # TODO: Gerçek sensör/hesaplama verilerini al
    return CockpitDashboard(
        thermal_harvest=ThermalHarvestData(
            motor_temperature_celsius=863.0,
            electron_order_percent=2.40,
            gaia_autonomous_power_days=1.22,
            timestamp=datetime.utcnow()
        ),
        ontological_reflex=OntologicalReflexData(
            shock_wave_detected=True,
            status="STABLE",
            reflex_time_seconds=0.000,
            fuel_saved_kg=0.00,
            timestamp=datetime.utcnow()
        ),
        national_balance=NationalBalanceData(
            aircraft_count=400,
            fund_usd=174_551_760.0,
            co2_prevented_tons=612_871.0,
            timestamp=datetime.utcnow()
        ),
        alignment="L = C.T",
        doi="10.5281/zenodo.18183914"
    )

@router.get("/thermal-harvest")
async def get_thermal_harvest() -> ThermalHarvestData:
    """Sadece termal hasat verileri"""
    # TODO: Gerçek motor sıcaklık sensörü
    return ThermalHarvestData(
        motor_temperature_celsius=863.0,
        electron_order_percent=2.40,
        gaia_autonomous_power_days=1.22,
        timestamp=datetime.utcnow()
    )

@router.get("/ontological-reflex")
async def get_ontological_reflex() -> OntologicalReflexData:
    """Sadece ontolojik refleks verileri"""
    # TODO: Gerçek şok dalgası algılama sistemi
    return OntologicalReflexData(
        shock_wave_detected=True,
        status="STABLE",
        reflex_time_seconds=0.000,
        fuel_saved_kg=0.00,
        timestamp=datetime.utcnow()
    )

@router.get("/national-balance")
async def get_national_balance() -> NationalBalanceData:
    """Sadece ulusal bilanço verileri"""
    # TODO: Gerçek bilanço hesaplamaları
    return NationalBalanceData(
        aircraft_count=400,
        fund_usd=174_551_760.0,
        co2_prevented_tons=612_871.0,
        timestamp=datetime.utcnow()
    )

# WebSocket for real-time updates
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    Real-time WebSocket connection.
    Frontend bağlanır ve sürekli güncel veri alır.
    """
    await websocket.accept()
    
    try:
        while True:
            # Her 1 saniyede güncel veri gönder
            dashboard_data = await get_dashboard()
            await websocket.send_json(dashboard_data.dict())
            await asyncio.sleep(1.0)
    
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()
```

### Phase 2: Core Processing Logic

**File**: `src/services/thermal_harvest.py`

```python
"""
Termal Hasat İşleme Servisi
Anayasa Madde 2.1 - Application Layer
"""

import asyncio
from datetime import datetime
from typing import Dict, Any

class ThermalHarvestProcessor:
    """
    Termal hasat hesaplamaları.
    
    Motor ısısı, elektron nizamı ve Gaia otonom güç
    hesaplamalarını yapar.
    """
    
    def __init__(self):
        self.base_temperature = 850.0  # °C
        self.electron_order_base = 2.0  # %
    
    async def calculate_motor_temperature(self) -> float:
        """
        Motor sıcaklığını hesapla.
        
        TODO: Gerçek sensör verisi entegrasyonu
        """
        # Simülasyon: Sinüs dalgası ile osilatif hareket
        import math
        t = datetime.utcnow().timestamp()
        variation = 13.0 * math.sin(t / 10.0)
        return self.base_temperature + variation
    
    async def calculate_electron_order(self) -> float:
        """
        Elektron nizamı yüzdesini hesapla.
        
        Returns:
            Elektron nizamı (%)
        """
        # TODO: Gerçek elektron nizamı algoritması
        import random
        return self.electron_order_base + random.uniform(-0.5, 0.5)
    
    async def calculate_gaia_power(self) -> float:
        """
        Gaia otonom güç süresini hesapla (gün).
        
        Returns:
            Kalan güç süresi (gün)
        """
        # TODO: Enerji tüketim modeli
        return 1.22  # Sabit değer (şimdilik)
    
    async def get_thermal_harvest_data(self) -> Dict[str, Any]:
        """Tüm termal hasat verilerini topla"""
        return {
            "motor_temperature_celsius": await self.calculate_motor_temperature(),
            "electron_order_percent": await self.calculate_electron_order(),
            "gaia_autonomous_power_days": await self.calculate_gaia_power(),
            "timestamp": datetime.utcnow().isoformat()
        }
```

**File**: `src/services/ontological_reflex.py`

```python
"""
Ontolojik Refleks Sistemi
Şok dalgası algılama ve tepki mekanizması
"""

import asyncio
from datetime import datetime
from typing import Dict, Any, Optional

class OntologicalReflexSystem:
    """
    Ontolojik refleks motoru.
    
    Şok dalgalarını algılar ve anlık tepki verir.
    Anayasa Madde 9.1: Refleks süresi hedefi <100ms
    """
    
    def __init__(self):
        self.shock_wave_threshold = 0.5
        self.last_detection_time: Optional[datetime] = None
        self.total_fuel_saved = 0.0
    
    async def detect_shock_wave(self) -> bool:
        """
        Şok dalgası algıla.
        
        Returns:
            True if shock wave detected
        """
        # TODO: Gerçek sensör entegrasyonu
        # Simülasyon: Rastgele algılama
        import random
        return random.random() > 0.7
    
    async def calculate_reflex_time(self) -> float:
        """
        Refleks tepki süresini hesapla.
        
        Returns:
            Süre (saniye)
        """
        # M2 Neural Engine ile hedef: <0.001 saniye
        return 0.000  # Teorik minimum
    
    async def calculate_fuel_saved(self, shock_intensity: float) -> float:
        """
        Kurtarılan yakıt miktarını hesapla.
        
        Args:
            shock_intensity: Şok yoğunluğu (0-1)
            
        Returns:
            Yakıt miktarı (kg)
        """
        # Formül: intensity * base_fuel_rate
        base_rate = 0.5  # kg per shock
        fuel = shock_intensity * base_rate
        self.total_fuel_saved += fuel
        return fuel
    
    async def get_reflex_data(self) -> Dict[str, Any]:
        """Ontolojik refleks verilerini topla"""
        shock_detected = await self.detect_shock_wave()
        
        if shock_detected:
            self.last_detection_time = datetime.utcnow()
            reflex_time = await self.calculate_reflex_time()
            fuel_saved = await self.calculate_fuel_saved(0.8)
        else:
            reflex_time = 0.0
            fuel_saved = 0.0
        
        return {
            "shock_wave_detected": shock_detected,
            "status": "STABLE" if shock_detected else "MONITORING",
            "reflex_time_seconds": reflex_time,
            "fuel_saved_kg": fuel_saved,
            "timestamp": datetime.utcnow().isoformat()
        }
```

### Phase 3: Frontend Integration (JavaScript)

**Update Netlify site to fetch from backend**:

```javascript
// public/js/dashboard.js

const API_BASE_URL = 'https://your-m2-server.com/api/v1/cockpit';
const UPDATE_INTERVAL = 1000; // 1 second

// Fetch dashboard data
async function fetchDashboardData() {
    try {
        const response = await fetch(`${API_BASE_URL}/dashboard`);
        const data = await response.json();
        updateDashboard(data);
    } catch (error) {
        console.error('Error fetching dashboard:', error);
    }
}

// Update DOM elements
function updateDashboard(data) {
    // Termal Hasat
    document.getElementById('motor-temp').textContent = 
        `${data.thermal_harvest.motor_temperature_celsius.toFixed(0)}°C`;
    
    document.getElementById('electron-order').textContent = 
        `+%${data.thermal_harvest.electron_order_percent.toFixed(2)}`;
    
    document.getElementById('gaia-power').textContent = 
        `${data.thermal_harvest.gaia_autonomous_power_days.toFixed(2)} GÜN`;
    
    // Ontolojik Refleks
    document.getElementById('shock-status').textContent = 
        data.ontological_reflex.shock_wave_detected ? '⚠️ ŞOK DALGASI ALGILANDI!' : '✓ NORMAL';
    
    document.getElementById('reflex-status').textContent = 
        data.ontological_reflex.status;
    
    document.getElementById('reflex-time').textContent = 
        `${data.ontological_reflex.reflex_time_seconds.toFixed(3)} SN`;
    
    document.getElementById('fuel-saved').textContent = 
        `${data.ontological_reflex.fuel_saved_kg.toFixed(2)} KG`;
    
    // Ulusal Bilanço
    document.getElementById('fund').textContent = 
        `$${data.national_balance.fund_usd.toLocaleString()}`;
    
    document.getElementById('co2-prevented').textContent = 
        `${data.national_balance.co2_prevented_tons.toLocaleString()} TON`;
}

// WebSocket real-time connection (alternative)
function connectWebSocket() {
    const ws = new WebSocket(`wss://your-m2-server.com/api/v1/cockpit/ws`);
    
    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        updateDashboard(data);
    };
    
    ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        // Fallback to REST polling
        startPolling();
    };
}

// Start polling
function startPolling() {
    setInterval(fetchDashboardData, UPDATE_INTERVAL);
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    // Try WebSocket first, fallback to polling
    try {
        connectWebSocket();
    } catch {
        startPolling();
    }
});
```

---

## 🔧 Deployment Options

### Option 1: Netlify Functions (Serverless)

Deploy backend as Netlify Functions:

```
fazz4webb1.netlify.app/
├── index.html          (existing)
├── netlify/
│   └── functions/
│       ├── dashboard.js
│       ├── thermal.js
│       └── reflex.js
```

**Pros**:
- Same domain (no CORS)
- Auto-scaling
- No server management

**Cons**:
- Cold start latency
- Limited to Node.js (need to port Python code)

### Option 2: Separate FastAPI Backend (Mac M2)

Run FastAPI on Mac M2, expose via ngrok/tunnel:

```bash
# On Mac M2
uvicorn src.interfaces.api.main:app --host 0.0.0.0 --port 8000

# Expose with ngrok
ngrok http 8000
# Get URL: https://xyz.ngrok.io
```

**Pros**:
- Full Python power
- M2 optimizations active
- Real-time calculations

**Cons**:
- Need to manage server
- May need static IP/domain

### Option 3: Hybrid (Recommended)

- **Frontend**: Netlify (static)
- **Backend**: Mac M2 FastAPI
- **Connection**: Cloudflare Tunnel or Tailscale

---

## 📊 Data Flow Example

### Request Flow

```
1. User opens fazz4webb1.netlify.app
   │
2. JavaScript fetches from API
   GET https://api.fazz4.com/cockpit/dashboard
   │
3. FastAPI (Mac M2) receives request
   └── cockpit_routes.py
       │
4. Calls service layer
   └── thermal_harvest.py
   └── ontological_reflex.py
       │
5. Services call protocol engine
   └── src/core/protocol_engine.py
       │
6. Real-time calculations (M2 optimized)
   - Motor temp: NumPy calculations
   - Reflex time: Neural Engine (if ML)
   - CO2 balance: Pandas aggregations
       │
7. Return JSON response
   │
8. Frontend updates DOM
   └── User sees live data
```

---

## 🎯 Implementation Checklist

### Backend (Mac M2)

- [ ] Create `src/interfaces/api/routes/cockpit.py`
- [ ] Create `src/services/thermal_harvest.py`
- [ ] Create `src/services/ontological_reflex.py`
- [ ] Create `src/services/national_balance.py`
- [ ] Add CORS middleware for Netlify domain
- [ ] Add WebSocket support
- [ ] Deploy FastAPI server
- [ ] Expose via tunnel/ngrok

### Frontend (Netlify)

- [ ] Add JavaScript fetch logic
- [ ] Update HTML to use dynamic data
- [ ] Add WebSocket fallback
- [ ] Test CORS
- [ ] Deploy to Netlify

### Testing

- [ ] Test REST endpoints
- [ ] Test WebSocket connection
- [ ] Load test (1000 req/s target)
- [ ] Latency test (< 100ms target)
- [ ] M2 performance validation

---

## 🚀 Quick Start

### 1. Add API Route

```bash
cd fazz4-system
mkdir -p src/interfaces/api/routes
# Copy cockpit.py code above to src/interfaces/api/routes/cockpit.py
```

### 2. Update Main API

```python
# src/interfaces/api/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.interfaces.api.routes import cockpit

app = FastAPI(title="FAZZ-4 API")

# CORS for Netlify
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://fazz4webb1.netlify.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include cockpit routes
app.include_router(cockpit.router)
```

### 3. Run Server

```bash
uvicorn src.interfaces.api.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Test

```bash
curl http://localhost:8000/api/v1/cockpit/dashboard
```

---

## 📝 Notes

- **DOI**: 10.5281/zenodo.18183914 should be included in all responses
- **Alignment**: "L = C.T" is a key system parameter
- **Real-time**: Target update rate is 1 Hz (1 update/second)
- **Performance**: Anayasa Madde 9.1 - API response < 100ms

---

**Integration Ready**: Backend structure prepared  
**Next Step**: Implement service logic with real calculations  
**Deployment**: Mac M2 FastAPI + Netlify frontend
