use project2;

 #1-- 
 SELECT p.SSN, p.NAME, COUNT(distinct StayID), SUM(t.COST)
 FROM patient p, treatment t, undergoes u, stay s
 WHERE p.age >= 30 AND p.age <= 40 AND strcmp(p.gender, "male") = 0 AND p.SSN = u.Patient AND t.Code = u.Treatment AND s.Patient = p.SSN AND s.StayID = u.Stay
 GROUP BY p.SSN
 HAVING COUNT(distinct StayID) > 1; 

 #2--
 SELECT n.EmployeeID, n.name
 FROM nurse n, on_call o
 WHERE n.EmployeeID = o.Nurse AND o.OnCallStart >= '2008-04-20 23:22:00' AND o.OnCallEnd <= '2009-06-04 11:00:00' AND o.BlockFloor >= 4 AND o.BlockFloor <= 7
 GROUP BY n.EmployeeID
 HAVING COUNT(*) > 1;

 #3-- 
 SELECT p.SSN, p.name, v.num_of_doses
 FROM vaccination v1, vaccines v, patient p
 WHERE p.age > 40 AND strcmp(p.gender, "female") = 0 AND strcmp(v1.vaccines_vax_name, v.vax_name) = 0 AND v1.patient_SSN = p.SSN
 GROUP BY p.SSN
 HAVING COUNT(*) = v.num_of_doses;

 #4-- 
 SELECT m.name, m.brand, COUNT(m.code)
 FROM medication m, prescribes pr
 WHERE m.code = pr.medication 
 GROUP BY m.code
 HAVING COUNT(m.code) > 1;

 #5-- 
 SELECT p.SSN, p.name
 FROM vaccination v1, patient p, physician ph
 WHERE v1.patient_SSN = p.SSN AND v1.physician_EmployeeID = ph.EmployeeID
 GROUP BY p.SSN
 HAVING COUNT(distinct(ph.EmployeeID)) = 1;
 
 #6-- 
 SELECT "yes" WHERE EXISTS(SELECT r.RoomNumber, COUNT(r.RoomNumber)
 FROM room r, stay s
 WHERE r.RoomNumber = s.Room AND StayStart >= '2013-01-01' AND StayEnd <= '2013-12-31'
 GROUP BY r.RoomNumber
 ORDER BY r.RoomNumber)
 UNION
 SELECT "no" WHERE NOT EXISTS(SELECT r.RoomNumber, COUNT(r.RoomNumber)
 FROM room r, stay s
 WHERE r.RoomNumber = s.Room AND StayStart >= '2013-01-01' AND StayEnd <= '2013-12-31'
 GROUP BY r.RoomNumber
 ORDER BY r.RoomNumber);

 #7-- 
 SELECT ph.EmployeeID, ph.name, COUNT(*)
 FROM physician ph, trained_in t, treatment tr, undergoes u
 WHERE ph.EmployeeID = t.Physician AND t.speciality = tr.Code AND strcmp(tr.name, 'PATHOLOGY') = 0 AND u.physician = ph.EmployeeID
 GROUP BY ph.EmployeeID
 UNION
 SELECT ph.EmployeeID, ph.name, 0
 FROM physician ph, trained_in t, treatment tr
 WHERE ph.EmployeeID = t.Physician AND t.speciality = tr.Code AND strcmp(tr.name, 'PATHOLOGY') = 0 AND (ph.EmployeeID NOT IN (SELECT u.physician FROM undergoes u))
 GROUP BY ph.EmployeeID;

#8-- 
 SELECT p.name
 FROM vaccination v1, vaccines v, patient p
 WHERE strcmp(v1.vaccines_vax_name, v.vax_name) = 0 AND v1.patient_SSN = p.SSN
 GROUP BY p.SSN
 HAVING COUNT(*) < 2
 UNION
 SELECT p.name
 FROM vaccination v1, patient p
 WHERE p.SSN NOT IN (SELECT v1.patient_SSN FROM vaccination v1);
 

#9-- 
SELECT v.vax_name
FROM vaccines v, vaccination vc
WHERE strcmp(v.vax_name, vc.vaccines_vax_name) = 0 
GROUP BY vc.vaccines_vax_name
HAVING COUNT(vc.vaccines_vax_name) >= ALL(	SELECT COUNT(vc.vaccines_vax_name) 
											FROM vaccines v, vaccination vc
											WHERE strcmp(v.vax_name, vc.vaccines_vax_name) = 0 
											GROUP BY vc.vaccines_vax_name );

#10-- 
SELECT DISTINCT(ph.name) FROM physician ph
WHERE not exists (SELECT* FROM treatment t WHERE strcmp(t.name, 'RADIATION ONCOLOGY') = 0
AND NOT EXISTS (SELECT* FROM trained_in tr WHERE tr.physician = ph.EmployeeID AND t.Code = tr.Speciality)); 

SELECT count(bl.BlockCode)
FROM block bl
WHERE bl.BlockFloor = 100;

SELECT ph.Name, nr.Name, tr.Cost, st.StayEnd, st.Room , r.BlockFloor, r.BlockCode
FROM Physician ph, Undergoes u, Patient p, Nurse nr, Treatment tr , Stay st , Room r
WHERE strcmp(p.Name, 'Koch Mercedes') = 0 and u.Patient = p.SSN and u.Physician = ph.EmployeeID and u.AssistingNurse = nr.EmployeeID and u.Treatment = tr.Code and st.StayID = u.stay  and st.Room = r.RoomNumber;





