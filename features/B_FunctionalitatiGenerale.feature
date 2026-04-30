Feature: Functionalitati Generale

  Background: Aplicatia ruleaza

    @FG_005
    Scenario: Testarea functionalitati SORTARE PRODUSE
      Given utilizatorul se afla pe Pagina Principala
      When se actioneaza butonul FILTRE si se alege optiunea A to Z
      Then produsele afisate pe pagina sunt sortate in ordine alfabetica
      When se actioneaza butonul FILTRE si se alege optiunea PRICE low to high
      Then produsele afisate pe pagina sunt sortate in ordine crescatoare in functie de pret


    @FG_006
    Scenario: Testarea functionalitati ADAUGARE IN COSUL de cumparaturi
      Given utilizatorul se afla pe Pagina Principala
      When se actioneaza butonul ADD TO CART aferent produsului de interes
      Then produsul de referinta se afla in cosul de cumparaturi

    @FG_007
    Scenario: Testarea functionalitati ELIMINARE DIN COSUL de cumparaturi
      Given utilizatorul se afla pe Pagina Cosului de cumparaturi unde are adaugat cel putin un produs
      When se actioneaza butonul REMOVE aferent produsului de interes
      Then produsul de referinta NU se mai afla in cosul de cumparaturi

    @FG_008
    Scenario: Testare afisarii SUMEI CORECTE pentru produsele adaugate in cosul de cumparaturi
      Given in cosul de cumparaturi sunt adaugate cel putin doua produse
      When se aduna preturile produselor pentru a obtine suma acestora si se urmeaza pasii pentru finalizarea comenzii pana in pasul in care este afisata suma total (Price Total)
      Then suma preturilor este egala cu cea afisata la rubrica suma total (Price Total)

    @FG_009
    Scenario: Testare functionalitati finalizare comanda
      Given in cosul de cumparaturi este adaugat cel putin un produs
      When se actioneaza butonul Checkout
      Then utilizatorul este directionat catre pagina in care este solicitata furnizarea datelor personale (nume, prenume si cod postal)
      When se insereaza datele personale in campurile aferente (nume, prenume si cod postal) si se actioneaza butonul Continue
      Then utilizatorul este directionat catre pagina de previzualizare a comenzii
      When se actioneaza butonul Finish
      Then pe ecran este afisat un mesaj care indica faptul ca procesul a fost finalizat cu succes

