import pathlib
from vcr import VCR

CASSETTE_LIBRARY = pathlib.Path(__file__).parent.resolve() / "vcr"
vcr = VCR(
    serializer="yaml",
    cassette_library_dir=str(CASSETTE_LIBRARY),
    record_mode="ONCE",
    match_on=["uri", "method", "query", "raw_body"],
    decode_compressed_response=True,
)
