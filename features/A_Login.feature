Feature: Functionalitate autentificare

  Background: Aplicatia ruleaza

    @Login_001
    Scenario: Testarea autentificarii utilizand CREDENTIALE VALIDE in campurile USERNAME si PASSWORD
      Given utilizatorul se afla pe Pagina de Autentificare
      When se insereaza credentiale valide in campurile USERNAME, respectiv PASSWORD si se actioneaza butonul LOGIN
      Then utilizatorul este autentificat cu succes si este directionat pe Pagina Principala

    @Login_002
    Scenario: Testarea autentificarii utilizand CREDENTIALE INVALIDE in campurile USERNAME si PASSWORD
      Given utilizatorul se afla pe Pagina de Autentificare
      When se insereaza credentiale invalide in campurile USERNAME, respectiv PASSWORD si se actioneaza butonul LOGIN
      Then pe ecran este afisat un mesaj de eroare care indica faptul ca datele inserate nu sunt valide

    @Login_003
    Scenario: Testarea functionalitatii de deautentificarii
      Given utilizatorul se afla pe Pagina Principala
      When se actioneaza butonul de tip burger din partea stanga-sus, iar din optiunile alese se actioneaza butonul LOGOUT
      Then utilizatorul este deautentificat si este directionat catre Pagina de Autentificare

    @Login_004
    Scenario: Testarea autentificarii utilizand credentialele unui utilzator care a fost BLOCAT
      Given utilizatorul se afla pe Pagina de Autentificare
      When se insereaza credentiale unui utilizator care a fost BLOCAT in campurile USERNAME, respectiv PASSWORD si se actioneaza butonul LOGIN
      Then pe ecran este afisat un mesaj de eroare care indica faptul ca utilizatorul a fost BLOCAT