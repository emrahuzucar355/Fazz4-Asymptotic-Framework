# FAZZ-4 Dual Web Applications - Unified Backend Architecture

**Date**: 2025-01-28  
**Applications**: 2 Live Web Interfaces  
**Backend**: fazz4-system (Mac M2)  
**DOI**: 10.5281/zenodo.18183914

---

## 🌐 Live Applications Overview

### Application 1: MASTER COCKPIT
**URL**: https://fazz4webb1.netlify.app  
**Type**: Comprehensive Dashboard  
**Purpose**: Full system monitoring and control

**Metrics Displayed**:
- **Termal Hasat (Pasif)**:
  - Motor Isisi: 863°C
  - Elektron Nizami: +%2.40
  - Gaia Otonom Güç: 1.22 gün

- **Ontolojik Refleks (Aktif)**:
  - Şok Dalgası Algılama
  - Refleks Süresi: 0.000 sn
  - Kurtarılan Yakıt: 0.00 kg

- **Ulusal Hasat Bilançosu (400 Uçak)**:
  - Fon: $174,551,760
  - Engellenen CO2: 612,871 ton

**Alignment**: L = C.T

### Application 2: BLUE HELIX [CORE]
**URL**: https://fazz4-live-organism.netlify.app  
**Type**: Minimalist System Monitor  
**Purpose**: Core protocol status

**Metrics Displayed**:
- **Protokol**: BLUE HELIX
- **Formül**: C = l.t (SÜRTÜNMESİZ)
- **Isı**: 31.0°C [STABİL]
- **Yük**: %40 [AKIŞKAN]

---

## 🏗️ Unified Backend Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     WEB APPLICATIONS                         │
│                                                              │
│  ┌──────────────────────┐    ┌──────────────────────┐      │
│  │  MASTER COCKPIT      │    │  BLUE HELIX [CORE]   │      │
│  │  fazz4webb1          │    │  fazz4-live-organism │      │
│  └──────────┬───────────┘    └──────────┬───────────┘      │
└─────────────┼──────────────────────────┼──────────────────┘
              │                           │
              │ REST/WebSocket            │ REST/WebSocket
              │                           │
┌─────────────▼───────────────────────────▼──────────────────┐
│              FAZZ-4 UNIFIED API GATEWAY                     │
│              (FastAPI - Mac M2)                             │
│                                                             │
│  ┌──────────────────┐    ┌──────────────────┐             │
│  │  /api/v1/cockpit │    │  /api/v1/helix   │             │
│  │  - dashboard      │    │  - status        │             │
│  │  - thermal        │    │  - core          │             │
│  │  - reflex         │    │  - formula       │             │
│  │  - balance        │    │                  │             │
│  └────────┬─────────┘    └────────┬─────────┘             │
└───────────┼──────────────────────┼─────────────────────────┘
            │                      │
            └──────────┬───────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│              APPLICATION LAYER (Services)                    │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Thermal    │  │ Ontological  │  │  Blue Helix  │     │
│  │   Harvest    │  │   Reflex     │  │   Engine     │     │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘     │
└─────────┼──────────────────┼──────────────────┼─────────────┘
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────┐
│                    DOMAIN LAYER                              │
│                 (Protocol Engine - Core)                     │
│                                                              │
│  • Unified Protocol Processing                              │
│  • M2-Optimized Calculations                                │
│  • Real-time State Management                               │
└──────────────────────────────────────────────────────────────┘
```

---

## 🚀 Implementation

### 1. Unified API Gateway

**File**: `src/interfaces/api/main.py`

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.interfaces.api.routes import cockpit, helix

app = FastAPI(
    title="FAZZ-4 Unified API",
    description="Backend for Master Cockpit & Blue Helix",
    version="1.0.0"
)

# CORS for both Netlify apps
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://fazz4webb1.netlify.app",
        "https://fazz4-live-organism.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include both route modules
app.include_router(cockpit.router, prefix="/api/v1")
app.include_router(helix.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "system": "FAZZ-4 Unified API",
        "doi": "10.5281/zenodo.18183914",
        "applications": [
            {
                "name": "Master Cockpit",
                "url": "https://fazz4webb1.netlify.app",
                "endpoints": "/api/v1/cockpit"
            },
            {
                "name": "Blue Helix [Core]",
                "url": "https://fazz4-live-organism.netlify.app",
                "endpoints": "/api/v1/helix"
            }
        ]
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "platform": "Apple Silicon M2",
        "architecture": "arm64"
    }
```

### 2. Blue Helix API Routes

**File**: `src/interfaces/api/routes/helix.py`

```python
"""
Blue Helix [Core] API Routes
Minimalist protocol monitoring endpoint
"""

from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Literal

router = APIRouter(prefix="/helix", tags=["blue-helix"])


class BlueHelixStatus(BaseModel):
    """Blue Helix core status"""
    protocol: str = "BLUE HELIX"
    formula: str = "C = l.t"
    formula_type: str = "SÜRTÜNMESİZ"  # Frictionless
    temperature_celsius: float
    temperature_status: Literal["STABİL", "YÜKSELİYOR", "DÜŞÜYORr"]
    load_percent: float
    load_status: Literal["AKIŞKAN", "YOĞUNLAşIYOR", "KRİTİK"]
    timestamp: datetime


@router.get("/status", response_model=BlueHelixStatus)
async def get_helix_status() -> BlueHelixStatus:
    """
    Get Blue Helix core status.
    
    This endpoint provides the minimalist protocol monitoring data
    displayed on https://fazz4-live-organism.netlify.app
    
    Returns:
        BlueHelixStatus: Current system status
    """
    # TODO: Real sensor data integration
    temperature = await _get_core_temperature()
    load = await _get_system_load()
    
    return BlueHelixStatus(
        protocol="BLUE HELIX",
        formula="C = l.t",
        formula_type="SÜRTÜNMESİZ",
        temperature_celsius=temperature,
        temperature_status=_get_temperature_status(temperature),
        load_percent=load,
        load_status=_get_load_status(load),
        timestamp=datetime.utcnow()
    )


@router.get("/core")
async def get_core_metrics():
    """
    Detailed core metrics for Blue Helix protocol.
    
    Returns:
        dict: Core system metrics
    """
    return {
        "protocol": {
            "name": "BLUE HELIX",
            "version": "1.0.0",
            "alignment": "C = l.t",
            "friction_coefficient": 0.0
        },
        "thermal": {
            "core_temperature": await _get_core_temperature(),
            "ambient_temperature": 22.0,
            "thermal_efficiency": 0.95
        },
        "load": {
            "current_percent": await _get_system_load(),
            "max_capacity": 100.0,
            "fluid_state": "AKIŞKAN"
        },
        "stability": {
            "oscillation_amplitude": 0.01,
            "resonance_frequency": 1.0,
            "damping_ratio": 0.7
        }
    }


# Helper functions
async def _get_core_temperature() -> float:
    """
    Calculate core temperature.
    Blue Helix operates at lower temps than Master Cockpit.
    
    Returns:
        Temperature in Celsius
    """
    # TODO: Real sensor integration
    # Blue Helix: 25-35°C range (vs Master Cockpit 850-880°C)
    import random
    return 31.0 + random.uniform(-2.0, 2.0)


async def _get_system_load() -> float:
    """
    Calculate system load percentage.
    
    Returns:
        Load as percentage (0-100)
    """
    # TODO: Real system metrics
    import random
    return 40.0 + random.uniform(-5.0, 5.0)


def _get_temperature_status(temp: float) -> Literal["STABİL", "YÜKSELİYOR", "DÜŞÜYORr"]:
    """Determine temperature status"""
    if 29.0 <= temp <= 33.0:
        return "STABİL"
    elif temp > 33.0:
        return "YÜKSELİYOR"
    else:
        return "DÜŞÜYORr"


def _get_load_status(load: float) -> Literal["AKIŞKAN", "YOĞUNLAşIYOR", "KRİTİK"]:
    """Determine load status"""
    if load < 60.0:
        return "AKIŞKAN"
    elif load < 85.0:
        return "YOĞUNLAşIYOR"
    else:
        return "KRİTİK"
```

### 3. Blue Helix Service Layer

**File**: `src/services/blue_helix_engine.py`

```python
"""
Blue Helix Engine Service
Application Layer - Anayasa Madde 2.1

The Blue Helix protocol is a frictionless (sürtünmesiz) energy
management system operating at lower temperatures than the main
thermal harvest system.
"""

import asyncio
import math
from datetime import datetime
from typing import Dict, Any, Tuple


class BlueHelixEngine:
    """
    Blue Helix protocol engine.
    
    Implements the C = l.t formula (frictionless coefficient).
    Operates in the 25-35°C range for optimal energy flow.
    """
    
    def __init__(self):
        self.base_temperature = 31.0  # °C
        self.base_load = 40.0  # %
        self.friction_coefficient = 0.0  # Frictionless
        self.time_constant = 1.0  # seconds
    
    async def calculate_frictionless_coefficient(
        self,
        length: float,
        time: float
    ) -> float:
        """
        Calculate C = l.t formula.
        
        Args:
            length: Spatial parameter (l)
            time: Temporal parameter (t)
            
        Returns:
            Frictionless coefficient (C)
        """
        # C = l * t (simplified)
        return length * time
    
    async def get_core_temperature(self) -> float:
        """
        Calculate Blue Helix core temperature.
        
        Uses oscillating pattern around base temperature
        to simulate natural thermal fluctuations.
        
        Returns:
            Temperature in Celsius
        """
        # Sine wave oscillation
        t = datetime.utcnow().timestamp()
        amplitude = 2.0  # ±2°C variation
        frequency = 0.1  # Slow oscillation
        
        variation = amplitude * math.sin(2 * math.pi * frequency * t)
        temperature = self.base_temperature + variation
        
        return round(temperature, 1)
    
    async def get_system_load(self) -> float:
        """
        Calculate system load percentage.
        
        Load varies based on energy demand and flow state.
        
        Returns:
            Load percentage (0-100)
        """
        # Simulate load with noise
        import random
        noise = random.uniform(-5.0, 5.0)
        load = self.base_load + noise
        
        # Clamp to valid range
        return max(0.0, min(100.0, round(load, 1)))
    
    async def get_flow_state(self, load: float) -> str:
        """
        Determine fluid flow state based on load.
        
        Args:
            load: System load percentage
            
        Returns:
            Flow state: AKIŞKAN, YOĞUNLAşIYOR, or KRİTİK
        """
        if load < 60.0:
            return "AKIŞKAN"  # Fluid
        elif load < 85.0:
            return "YOĞUNLAşIYOR"  # Condensing
        else:
            return "KRİTİK"  # Critical
    
    async def calculate_energy_efficiency(
        self,
        temperature: float,
        load: float
    ) -> float:
        """
        Calculate energy efficiency of Blue Helix.
        
        Efficiency is highest when:
        - Temperature is near optimal (31°C)
        - Load is in fluid range (<60%)
        
        Args:
            temperature: Core temperature (°C)
            load: System load (%)
            
        Returns:
            Efficiency (0.0-1.0)
        """
        # Temperature factor
        optimal_temp = 31.0
        temp_deviation = abs(temperature - optimal_temp)
        temp_factor = max(0.0, 1.0 - temp_deviation / 10.0)
        
        # Load factor
        load_factor = max(0.0, 1.0 - load / 100.0)
        
        # Combined efficiency
        efficiency = 0.7 * temp_factor + 0.3 * load_factor
        
        return round(efficiency, 3)
    
    async def get_full_status(self) -> Dict[str, Any]:
        """
        Get complete Blue Helix status.
        
        Returns:
            Complete system status dictionary
        """
        temperature = await self.get_core_temperature()
        load = await self.get_system_load()
        flow_state = await self.get_flow_state(load)
        efficiency = await self.calculate_energy_efficiency(temperature, load)
        
        # Calculate frictionless coefficient
        # Using arbitrary l and t for demonstration
        coefficient = await self.calculate_frictionless_coefficient(
            length=1.0,
            time=1.0
        )
        
        return {
            "protocol": {
                "name": "BLUE HELIX",
                "formula": "C = l.t",
                "friction": self.friction_coefficient
            },
            "thermal": {
                "temperature_celsius": temperature,
                "optimal_range": [29.0, 33.0],
                "status": self._get_temp_status(temperature)
            },
            "load": {
                "percent": load,
                "state": flow_state,
                "capacity_remaining": 100.0 - load
            },
            "efficiency": efficiency,
            "coefficient": coefficient,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def _get_temp_status(self, temp: float) -> str:
        """Helper: Get temperature status"""
        if 29.0 <= temp <= 33.0:
            return "STABİL"
        elif temp > 33.0:
            return "YÜKSELİYOR"
        else:
            return "DÜŞÜYORr"


# Global instance
blue_helix = BlueHelixEngine()
```

### 4. Frontend Integration

#### Blue Helix Frontend (JavaScript)

```javascript
// For https://fazz4-live-organism.netlify.app

const API_URL = 'https://your-m2-server.com/api/v1/helix';
const UPDATE_INTERVAL = 2000; // 2 seconds (slower than cockpit)

async function updateBlueHelixStatus() {
    try {
        const response = await fetch(`${API_URL}/status`);
        const data = await response.json();
        
        // Update DOM
        document.getElementById('temperature').textContent = 
            `${data.temperature_celsius}°C [${data.temperature_status}]`;
        
        document.getElementById('load').textContent = 
            `%${data.load_percent} [${data.load_status}]`;
        
        document.getElementById('formula').textContent = 
            `${data.formula} (${data.formula_type})`;
        
    } catch (error) {
        console.error('Error fetching Blue Helix status:', error);
    }
}

// Start periodic updates
setInterval(updateBlueHelixStatus, UPDATE_INTERVAL);

// Initial load
document.addEventListener('DOMContentLoaded', updateBlueHelixStatus);
```

---

## 📊 Data Comparison

### Temperature Scales

| System | Operating Range | Purpose |
|--------|----------------|---------|
| **Master Cockpit** | 850-880°C | High-intensity thermal harvest |
| **Blue Helix** | 29-33°C | Low-temperature energy flow |

**Relationship**: Blue Helix may represent the cooling/regulation system for Master Cockpit.

### Alignment Formulas

| System | Formula | Meaning |
|--------|---------|---------|
| **Master Cockpit** | L = C.T | Light = Coefficient × Time |
| **Blue Helix** | C = l.t | Coefficient = length × time (frictionless) |

**Observation**: Both use similar symbolic notation but different parameters.

---

## 🔄 Integration Patterns

### Pattern 1: Independent Systems

```
Master Cockpit (High-energy) ⚡ → Independent monitoring
Blue Helix (Low-energy) 🌊 → Independent monitoring
```

**Use Case**: Two separate protocols running in parallel.

### Pattern 2: Hierarchical Relationship

```
Master Cockpit (Primary) 
    ↓ Energy regulation
Blue Helix (Secondary/Cooling)
```

**Use Case**: Blue Helix regulates/cools Master Cockpit output.

### Pattern 3: Complementary Systems

```
Hot Path: Master Cockpit (863°C)
           ↓ Heat exchange
Cold Path: Blue Helix (31°C)
           ↓ Frictionless flow
     Combined Efficiency
```

**Use Case**: Thermodynamic cycle with hot and cold reservoirs.

---

## 🎯 Unified Monitoring Dashboard

### Option: Create Third Application

**Concept**: Unified dashboard showing both systems

```
┌──────────────────────────────────────┐
│   FAZZ-4 UNIFIED COMMAND CENTER     │
├──────────────┬───────────────────────┤
│              │                       │
│  HOT SIDE    │    COLD SIDE         │
│              │                       │
│  Master      │    Blue Helix        │
│  Cockpit     │    [Core]            │
│              │                       │
│  863°C       │    31°C              │
│  L = C.T     │    C = l.t           │
│              │                       │
└──────────────┴───────────────────────┘
```

---

## 🚀 Deployment Checklist

### Backend (Mac M2)

- [x] Unified API gateway structure
- [ ] Implement `src/interfaces/api/routes/helix.py`
- [ ] Implement `src/services/blue_helix_engine.py`
- [ ] Update `src/interfaces/api/main.py` with both routers
- [ ] Add CORS for both Netlify domains
- [ ] Test both `/cockpit` and `/helix` endpoints
- [ ] Deploy on Mac M2

### Frontend Updates

#### Master Cockpit
- [ ] Add API fetch to `fazz4webb1.netlify.app`
- [ ] Update JavaScript for REST/WebSocket
- [ ] Test CORS
- [ ] Deploy to Netlify

#### Blue Helix
- [ ] Add API fetch to `fazz4-live-organism.netlify.app`
- [ ] Update JavaScript for status updates
- [ ] Test CORS
- [ ] Deploy to Netlify

### Testing

- [ ] Test `/api/v1/cockpit/dashboard`
- [ ] Test `/api/v1/helix/status`
- [ ] Test `/api/v1/helix/core`
- [ ] Load test both endpoints
- [ ] Cross-browser testing
- [ ] Mobile responsiveness

---

## 📝 API Endpoints Summary

### Master Cockpit Endpoints

```
GET  /api/v1/cockpit/dashboard       # Full dashboard
GET  /api/v1/cockpit/thermal-harvest # Thermal data only
GET  /api/v1/cockpit/ontological-reflex # Reflex data
GET  /api/v1/cockpit/national-balance   # Balance data
WS   /api/v1/cockpit/ws              # WebSocket real-time
```

### Blue Helix Endpoints

```
GET  /api/v1/helix/status            # Core status
GET  /api/v1/helix/core              # Detailed metrics
```

### System Endpoints

```
GET  /                               # API info
GET  /health                         # Health check
```

---

## 🎓 Key Insights

### Dual System Architecture

1. **Master Cockpit**: High-energy, complex monitoring
   - Multiple subsystems
   - National-scale metrics
   - Real-time reflexes

2. **Blue Helix**: Low-energy, minimalist core
   - Simple protocol
   - Frictionless operation
   - Fluid state monitoring

### Possible Interpretation

Blue Helix may represent:
- **Cooling system** for Master Cockpit
- **Energy regulation** layer
- **Frictionless transport** medium
- **Secondary protocol** for efficiency

---

## ✅ Implementation Priority

### Phase 1 (Week 1)
1. Set up unified API gateway
2. Implement Blue Helix routes
3. Basic data endpoints working

### Phase 2 (Week 2)
4. Frontend integration for both sites
5. WebSocket for Master Cockpit
6. REST polling for Blue Helix

### Phase 3 (Week 3)
7. Real sensor data integration
8. Performance optimization
9. M2-specific acceleration

### Phase 4 (Week 4)
10. Production deployment
11. Monitoring and alerting
12. Documentation finalization

---

**Status**: Architecture Ready ✅  
**Next Step**: Implement helix.py routes  
**Integration**: Dual-frontend, unified backend  
**Platform**: Mac M2 (ARM64 optimized)
