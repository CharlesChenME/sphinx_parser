import os
import warnings


def get_potential_path(element: str):
    """
    Get the path to the potential file for the given element.

    Args:
        element (str): The element symbol.

    Returns:
        str: The path to the potential file.
    """
    path = os.path.join(os.getenv("CONDA_PREFIX"), "share", "sphinxdft", "jth-gga-pbe")
    return os.path.join(path, f"{element}_GGA.atomicdata")


def _remove_hash_tag(text):
    """
    Remove all lines starting with a hash tag.

    Args:
        text (str): The text to process.

    Returns:
        str: The processed text.
    """
    result = re.sub(r"^#.*$", "", text, flags=re.MULTILINE)
    return re.sub(r"\n+", "\n", result).strip()


def _is_vasp_potential(file_content, min_hits=2):
    """
    Check if the file content is a VASP potential.

    Args:
        file_content (str): The content of the file.
        min_hits (int): The minimum number of expected terms.

    Returns:
        bool: True if the file content is a VASP potential.
    """
    exp_terms = ["Georg Kresse", "VASP", "PAW", "TITEL"]
    terms_404 = [term for term in exp_terms if term not in file_content]
    if len(terms_404) == 0:
        return True
    if len(exp_terms) - len(terms_404) > min_hits:
        warnings.warn(
            f"Potential file is a VASP potential, but missing terms: {terms_404}"
        )
        return True
    return False
