from src.m01_prima_entita_e_dataclass.es08.reference import CameraHotel


def test_check_in_su_camera_libera():
    cam = CameraHotel(101, "Doppia", 100.0)
    assert cam.is_occupata is False
    assert cam.check_in() is True
    assert cam.is_occupata is True


def test_check_in_su_camera_gia_occupata_fallisce():
    cam = CameraHotel(101, "Doppia", 100.0, is_occupata=True)
    assert cam.check_in() is False
    assert cam.is_occupata is True


def test_check_out_su_camera_occupata():
    cam = CameraHotel(101, "Doppia", 100.0, is_occupata=True)
    assert cam.check_out() is True
    assert cam.is_occupata is False


def test_check_out_su_camera_gia_libera_fallisce():
    cam = CameraHotel(101, "Doppia", 100.0, is_occupata=False)
    assert cam.check_out() is False
    assert cam.is_occupata is False


def test_sconto_valido_entro_il_50_percento():
    cam = CameraHotel(101, "Suite", 200.0)
    assert cam.applica_sconto(25.0) is True
    assert cam.tariffa_giornaliera == 150.0


def test_sconto_soglia_esatta_50_percento():
    cam = CameraHotel(101, "Suite", 200.0)
    assert cam.applica_sconto(50.0) is True
    assert cam.tariffa_giornaliera == 100.0


def test_sconto_superiore_al_50_percento_respinto():
    cam = CameraHotel(101, "Suite", 200.0)
    assert cam.applica_sconto(50.1) is False
    assert cam.applica_sconto(80.0) is False
    assert cam.tariffa_giornaliera == 200.0  # Tariffa intatta


def test_sconto_non_positivo_respinto():
    cam = CameraHotel(101, "Suite", 200.0)
    assert cam.applica_sconto(0.0) is False
    assert cam.applica_sconto(-15.0) is False
    assert cam.tariffa_giornaliera == 200.0
