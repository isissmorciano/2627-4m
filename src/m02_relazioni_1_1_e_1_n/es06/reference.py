from dataclasses import dataclass, field


@dataclass
class Studente:
    matricola: int
    nome: str
    media_voti: float


@dataclass
class ClasseScolastica:
    sezione: str
    capienza_massima: int = 25
    studenti: list[Studente] = field(default_factory=list)

    def iscrivi_studente(self, s: Studente) -> bool:
        if len(self.studenti) < self.capienza_massima:
            self.studenti.append(s)
            return True
        return False

    def calcola_media_classe(self) -> float:
        if not self.studenti:
            return 0.0
        return round(sum(s.media_voti for s in self.studenti) / len(self.studenti), 2)

    def elenco_promossi(self) -> list[str]:
        return [s.nome for s in self.studenti if s.media_voti >= 6.0]


def main() -> None:
    print("=== GESTIONALE SCOLASTICO (1:N) ===")
    classe: ClasseScolastica = ClasseScolastica(sezione="4A Informatica", capienza_massima=25)

    s1: Studente = Studente(101, "Mario Rossi", 7.5)
    s2: Studente = Studente(102, "Anna Bianchi", 5.5)
    s3: Studente = Studente(103, "Luca Verdi", 8.0)

    classe.iscrivi_studente(s1)
    classe.iscrivi_studente(s2)
    classe.iscrivi_studente(s3)

    print(f"Iscritto: {s1.nome} (Media: {s1.media_voti})")
    print(f"Iscritto: {s2.nome} (Media: {s2.media_voti})")
    print(f"Iscritto: {s3.nome} (Media: {s3.media_voti})\n")

    print(f"Media generale classe: {classe.calcola_media_classe():.2f}")
    print(f"Studenti promossi: {classe.elenco_promossi()}")


if __name__ == "__main__":
    main()
