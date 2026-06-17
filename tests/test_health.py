from app.services.health import get_health_status


def test_get_health_status_returns_healthy_status():
    health_status = get_health_status()

    assert health_status["service"] == "api-ingestion-pipeline"
    assert health_status["status"] == "healthy"
    assert "timestamp" in health_status
    assert health_status["checks"]["validation"] == "available"
