from dataclasses import dataclass


@dataclass
class Studente:
    matricola: int
    nome: str


@dataclass
class Corso:
    codice_corso: str
    titolo: str
    cfu: int


@dataclass
class Iscrizione:
    id: int
    studente: Studente
    corso: Corso
    data_iscrizione: str
    voto_esame: int | None = None

    def verbalizza_voto(self, voto: int) -> bool:
        if 18 <= voto <= 30:
            self.voto_esame = voto
            return True
        return False

    def is_superato(self) -> bool:
        return self.voto_esame is not None and self.voto_esame >= 18


def main() -> None:
    print("=== GESTIONALE UNIVERSITA (RELAZIONE N:N) ===")
    alice = Studente(1001, "Alice")
    cs101 = Corso("CS101", "Architettura Software", 6)

    iscrizione = Iscrizione(1, alice, cs101, "2026-10-01")

    print(f"Studente: {alice.nome} (Matricola {alice.matricola})")
    print(f"Corso: {cs101.codice_corso} ({cs101.titolo}, {cs101.cfu} CFU)\n")
    print(f"Iscrizione registrata in data: {iscrizione.data_iscrizione}")
    print(f"Stato esame iniziale: Superato? {iscrizione.is_superato()} (Voto: {iscrizione.voto_esame})\n")

    es1 = iscrizione.verbalizza_voto(15)
    print(f"Tentativo verbalizzazione voto 15 (insufficiente) -> Esito: {es1}")

    es2 = iscrizione.verbalizza_voto(28)
    print(f"Verbalizzazione voto 28 -> Esito: {es2}")
    print(f"Stato finale esame: Superato? {iscrizione.is_superato()} (Voto: {iscrizione.voto_esame})")


if __name__ == "__main__":
    main()
