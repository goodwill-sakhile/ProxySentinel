class RuleValidator:
    """
    Validates rule formats.
    """
    def __init__(self):
        pass

    def validate_ip(self, ip):
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return False
        return True

    def validate_keyword(self, keyword):
        return isinstance(keyword, str) and len(keyword.strip()) > 0
