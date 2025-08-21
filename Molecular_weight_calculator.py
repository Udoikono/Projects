from chempy import Substance
# from rdkit import Chem
# from rdkit.Chem import Descriptors
#
#
# def molar_weight(value) -> float:
#     formula = formula_to_smiles[value]
#     mol = Chem.MolFromSmiles(formula)
#     if not mol:
#         raise ValueError('Invalid formula')
#     return Descriptors.MolWt(mol)
#
#
# if __name__ == '__main__':
#     print(molar_weight('CO2'))




def molar_weight(value: str = None) -> float:
    while True:
        try:
            value = input('Enter the formula: ')
            # Use provided value or prompt for input if None
            substance = Substance.from_formula(value)
                return substance.molar_mass()
        except Exception:
            print(f'Invalid formula: {value}')
            # Optionally, ask if user wants to retry
            retry = input('Try another formula? (y/n): ').lower()
            if retry != 'y':
                break
        continue

              # Reset value to prompt again

if __name__ == '__main__':
    print(molar_weight())  # Output: 44.009

    # Interactive example:
    # print(molar_weight())  # Prompts for input, e.g., 'CO2' -> 44.009
