from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, MACCSkeys


# 增强的特征工程
def S2FPS(smiles):
    mol = Chem.MolFromSmiles(smiles)
    ecfp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)
    return ecfp
    # return np.concatenate([ecfp, maccs])

def S2DES(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return [
        Descriptors.MolWt(mol),
        Descriptors.MolLogP(mol),
        Descriptors.NumHDonors(mol),
        Descriptors.NumHAcceptors(mol),
        Descriptors.TPSA(mol),
        Descriptors.NumRotatableBonds(mol),
        Descriptors.NumHeteroatoms(mol),
        Descriptors.NumAromaticRings(mol),
        Descriptors.FractionCSP3(mol),
    ]

def S2MAC(smiles):
    mol = Chem.MolFromSmiles(smiles)
    maccs = MACCSkeys.GenMACCSKeys(mol)
    return maccs