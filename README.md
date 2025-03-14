Online Sales Analysis 

Acest proiect este dedicat dezvoltării unui sistem de analiză a datelor de vânzări pentru un magazin online. Proiectul este dezvoltat în Python, folosind concepte avansate OOP și Git pentru controlul versiunilor și colaborarea în echipă.  


Structura Proiectului 

online_sales_analysis/
─ product.py           # Clasa Product pentru gestionarea produselor
─ product_manager.py   # Clasa ProductManager pentru administrarea produselor
─ cart.py              # Clasa Cart pentru gestionarea coșului de cumpărături
─ main.py              # Scriptul principal pentru testarea funcționalităților
─ .gitignore           # Fișier pentru excluderea datelor sensibile
─ README.md            # Documentația proiectului
─ config.json          # Fișier de testare pentru excludere în .gitignore


Funcționalități Cheie**  

1. `Product` (Definită în `product.py`)  

- Atribute: 
  - `name` - Numele produsului  
  - `price` - Prețul produsului  
  - `quantity` - Cantitatea disponibilă  

- Metode:  
  - `display_product_info()` - Afișează detalii despre produs.  
  - `update_quantity(new_quantity)` - Actualizează cantitatea produsului.  


2. `ProductManager` (Definită în `product_manager.py`) 
 
- Atribute: 
  - `products` - Listă care stochează toate produsele.  

- Metode: 
  - `add_product(product)` - Adaugă un nou produs în lista de produse.  
  - `display_products()` - Afișează toate produsele disponibile.  
  - `display_total_value()` - Afișează valoarea totală a inventarului.  
  - `remove_product(product_name)` - Șterge un produs după nume.  


3. `Cart` (Definită în `cart.py`)  

- Atribute:
  - `cart_items` - Listă de produse adăugate în coș.  

- Metode:  
  - `add_to_cart(product)` - Adaugă un produs în coș.  
  - `calculate_total()` - Calculează valoarea totală de plată.  
  - `display_cart()` - Afișează produsele din coș.  


4. `main.py`  

- Creează instanțe ale claselor `ProductManager` și `Cart`.  
- Adaugă produse, le afișează și calculează valoarea totală.  
- Simulează adăugarea produselor în coș și afișează conținutul și totalul coșului.  


Gestionarea Versiunilor cu Git 
 
- Proiectul a fost gestionat folosind Git și GitHub.  
- S-au utilizat ramuri separate pentru adăugarea de funcționalități:  
  - `add-product-removal` pentru adăugarea metodei de ștergere a produselor.  
  - `add-cart-functionality` pentru adăugarea coșului de cumpărături.  
- Conflictele apărute în timpul îmbinărilor au fost rezolvate manual.  


.gitignore 

Fișierul `.gitignore` a fost configurat pentru a exclude:  
- `config.json` (fișiere de configurare și date sensibile).  
- Capturile de ecran (`*.png`, `*.jpg`).  


Pași pentru Rulare 

1. Clonează repository-ul: 
```bash
git clone https://github.com/<username>/online_sales_analysis.git
cd online_sales_analysis
```

2. Rulează scriptul principal: 
```bash
python main.py
```


Date Sensibile
  
- `config.json` a fost creat doar pentru testare și este exclus prin `.gitignore`.  
- Exemplu de conținut:  
```json
{
    "api_key": "12345",
    "database_url": "localhost"
}
```


Link către Repository-ul GitHub 
 
[https://github.com/<username>/online_sales_analysis](https://github.com/<LeontescuRadu>/online_sales_analysis)  


Note Finale

- Fiecare etapă a fost documentată și testată.  
- Commit-urile conțin mesaje clare și semnificative.  
- Pentru orice întrebări sau clarificări, nu ezitați să mă contactați.  

