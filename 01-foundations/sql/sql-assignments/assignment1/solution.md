## Solution

```sql
SELECT * FROM patients WHERE year(birth_date) >= 2005;

SELECT last_name from patients WHERE last_name like '%A';

SELECT first_name, count(admission_date) as visits from physicians p JOIN admissions a ON p.physician_id = a.attending_physician_id GROUP BY first_name ORDER BY visits DESC LIMIT 1;

select count(*) FROM physicians WHERE specialty = "Cardiologist";

Select count(*) FROM admissions WHERE YEAR(admission_date) = 2018 AND month(admission_date) = 7;

select count(*) from admissions WHERE diagnosis = "Appendicitis";

SELECT city, count(patient_id) as num_patients from patients GROUP BY city ORDER BY num_patients DESC LIMIT 5;

SELECT allergies, count(patient_id) AS num_patients from patients WHERE allergies IS NOT NULL GROUP BY allergies ORDER BY num_patients DESC LIMIT 3;

SELECT avg(height) FROM patients WHERE gender = 'M' AND city = 'Dundas';

SELECT avg(height) FROM patients WHERE gender = 'F' AND allergies = 'Penicillin';

UPDATE patients SET allergies = 'Malar' WHERE allergies = 'Sulfa';
```