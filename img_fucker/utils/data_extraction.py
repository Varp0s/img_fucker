import re
from core.validation import ck_credit_card, ck_email, ck_domain, ck_url

def extract_sensitive_data(text: str):
    """
    Extract sensitive data filter from the given text.

    This function takes a text input and searches for various sensitive data filter
    using regular expressions. It supports filter like phone numbers, email addresses,
    URLs, credit card numbers, and more.

    Args:
        text (str): The input text to search for sensitive data filter.

    Returns:
        list: A list of dictionaries containing the found sensitive data and their types.
    """
    filter = {
        "PHONE_NUMBER": r"(^05\d{2})(\s|-)?(\d{3})(\s|-)?(\d{4})",
        "EMAIL":  r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b",
        "URL": r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        "CREDIT_CARD": r"\b\d{4}[\s\-]?\d{4}[\s\-]?\d{4}[\s\-]?\d{4}\b",
        "COMBOLIST": r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Z|a-z]{2,}):[^\s]+\b",
        "DATE": r"\b\d{2}/\d{2}/\d{4}\b",
        "DOMAIN": r"(?<!@)\b([a-zA-Z0-9-]+\.[a-zA-Z]{2,6})(?=\s|$|,)",
        "ID_NUMBER": r"\b\d{11}\b",
        "PLATE": r"\b([0-9]{2} [A-Z]{1,3} [0-9]{1,5})\b",
        "HASH_MD5": r"\b[a-fA-F0-9]{32}\b",
        "HASH_SHA1": r"\b[a-fA-F0-9]{40}\b",
        "HASH_SHA256": r"\b[a-fA-F0-9]{64}\b",
    }

    findings = []
    for data_type, pattern in filter.items():
        matches = re.findall(pattern, text)
        for match in matches:
            if isinstance(match, tuple):
                match = match[0]

            if data_type == "CREDIT_CARD":
                cleaned_credit_card = match.replace(" ", "").replace("-", "")
                if ck_credit_card.validate_credit_card_number(cleaned_credit_card):
                    findings.append({"value": match, "type": data_type})
            elif data_type == "EMAIL":
                email_verification_result = ck_email.fetch_email_verification(match)
                if email_verification_result and ck_email.is_email_deliverable(email_verification_result):
                    findings.append({"value": match, "type": data_type})
            elif data_type == "DOMAIN":
                if ck_domain.verify_domain(match):
                    findings.append({"value": match, "type": data_type})
            elif data_type in {"COMBOLIST", "DATE", "ID_NUMBER", "PLATE", "HASH_MD5", "HASH_SHA1", "HASH_SHA256"}:
                findings.append({"value": match, "type": data_type})

    return findings
