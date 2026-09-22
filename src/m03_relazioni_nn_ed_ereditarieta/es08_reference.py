class Motore:
    def __init__(self, cilindrata: int, tipo_carburante: str) -> None:
        self.cilindrata = cilindrata
        self.tipo_carburante = tipo_carburante


class Veicolo:
    def __init__(self, targa: str, marca: str, tariffa_base: float, motore: Motore | None = None) -> None:
        self.targa = targa
        self.marca = marca
        self.tariffa_base = tariffa_base
        self.motore = motore


class Furgone(Veicolo):
    def __init__(self, targa: str, marca: str, tariffa_base: float, capacita_carico_kg: int, motore: Motore | None = None) -> None:
        super().__init__(targa, marca, tariffa_base, motore)
        self.capacita_carico_kg = capacita_carico_kg


def main() -> None:
    print("=== ARCHITETTURA CORRETTA: HAS-A VS IS-A ===")
    motore_diesel = Motore(2000, "Diesel")
    furgone = Furgone("AB123CD", "Iveco", 80.0, capacita_carico_kg=1500, motore=motore_diesel)

    print(f"Furgone: {furgone.marca} (Targa {furgone.targa})")
    print(f"Carico massimo: {furgone.capacita_carico_kg} kg")
    print(f"Motore componente (HAS-A): {furgone.motore.cilindrata}cc ({furgone.motore.tipo_carburante})")
    print(f"Verifica ereditarieta (IS-A): Furgone e' un Veicolo? {isinstance(furgone, Veicolo)}")


if __name__ == "__main__":
    main()
