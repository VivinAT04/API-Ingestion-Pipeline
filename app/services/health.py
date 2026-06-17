from datetime import datetime, timezone


def get_health_status() -> dict:
    """
    Return a simple health status for the ingestion pipeline.
    """
    return {
        "service": "api-ingestion-pipeline",
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "checks": {
            "normalization": "available",
            "validation": "available",
            "storage": "available",
        },
    }
