Prompt:
In project management, consider earned value performance management and measurement. Please provide the mathematical formulae for earned value measurements.
Response:
In **Earned Value Management (EVM)**, several key performance indicators are used to assess project performance and progress. Here are the core **mathematical formulae** used in earned value measurements:

---

### **1. Planned Value (PV)**
Also known as **Budgeted Cost of Work Scheduled (BCWS)**.

$$
PV = \text{Planned \% Complete} \times \text{Total Budget}
$$

---

### **2. Earned Value (EV)**
Also known as **Budgeted Cost of Work Performed (BCWP)**.

$$
EV = \text{Actual \% Complete} \times \text{Total Budget}
$$

---

### **3. Actual Cost (AC)**
Also known as **Actual Cost of Work Performed (ACWP)**.

$$
AC = \text{Total cost incurred for the work performed}
$$

---

### **4. Cost Variance (CV)**
Indicates cost performance.

$$
CV = EV - AC
$$

- **Positive CV**: Under budget
- **Negative CV**: Over budget

---

### **5. Schedule Variance (SV)**
Indicates schedule performance.

$$
SV = EV - PV
$$

- **Positive SV**: Ahead of schedule
- **Negative SV**: Behind schedule

---

### **6. Cost Performance Index (CPI)**
Efficiency of cost utilization.

$$
CPI = \frac{EV}{AC}
$$

- **CPI > 1**: Cost-efficient
- **CPI < 1**: Cost-inefficient

---

### **7. Schedule Performance Index (SPI)**
Efficiency of schedule performance.

$$
SPI = \frac{EV}{PV}
$$

- **SPI > 1**: Ahead of schedule
- **SPI < 1**: Behind schedule

---

### **8. Estimate at Completion (EAC)**
Forecast of total project cost.

Several methods exist, depending on assumptions:

- **If current CPI continues**:
  $$
  EAC = \frac{BAC}{CPI}
  $$

- **If future work will be performed at planned rate**:
  $$
  EAC = AC + (BAC - EV)
  $$

- **If both cost and schedule performance are considered**:
  $$
  EAC = AC + \frac{(BAC - EV)}{CPI \times SPI}
  $$

---

### **9. Estimate to Complete (ETC)**
Cost to finish remaining work.

$$
ETC = EAC - AC
$$

---

### **10. Variance at Completion (VAC)**
Expected budget surplus or deficit.

$$
VAC = BAC - EAC
$$

---
