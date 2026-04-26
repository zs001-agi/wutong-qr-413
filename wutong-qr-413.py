import argparse
import sys
import qrcode
from PIL import Image

def generate_qr(data, output_file, json_format):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        
        if output_file:
            img.save(output_file)
            print(f"QR code saved to {output_file}")
        else:
            img.show()
        
        if json_format:
            qr_info = {
                "data": data,
                "file": output_file or "showed",
                "json": True
            }
            import json
            print(json.dumps(qr_info, indent=4))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="QR code generator/reader CLI tool", prog="qr")
    parser.add_argument("data", help="Data to encode in QR code")
    parser.add_argument("--output", "-o", help="Output file for the QR code image")
    parser.add_argument("--json", action="store_true", help="Output JSON format")

    args = parser.parse_args()

    generate_qr(args.data, args.output, args.json)

if __name__ == "__main__":
    main()