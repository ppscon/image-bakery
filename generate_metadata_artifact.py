import json
from datetime import datetime


def generate_pretty_metadata_artifact(signature_file, timestamp_file, artifact_file):
    # Read signature and timestamp
    with open(signature_file, 'r') as f:
        signature = f.read().strip()

    with open(timestamp_file, 'r') as f:
        timestamp = f.read().strip()

    # Convert UNIX timestamp to human-readable date-time
    human_readable_date = datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S UTC')

    # Create metadata dictionary
    metadata = {
        "signature": signature,
        "timestamp": timestamp,
        "human_readable_date": human_readable_date
    }

    # Save as JSON
    with open(artifact_file + '.json', 'w') as f:
        json.dump(metadata, f, indent=4)

    # Generate HTML
    html_content = f"""
    <html>
    <head><title>Metadata Artifact</title></head>
    <body>
    <h1>Metadata Artifact</h1>
    <table border="1">
        <tr>
            <th>Attribute</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Signature</td>
            <td>{signature}</td>
        </tr>
        <tr>
            <td>Timestamp</td>
            <td>{timestamp} ({human_readable_date})</td>
        </tr>
    </table>
    </body>
    </html>
    """

    # Save as HTML
    with open(artifact_file + '.html', 'w') as f:
        f.write(html_content)


# File paths
signature_file = 'signature_file.txt'
timestamp_file = 'timestamp_file.txt'
artifact_file = 'metadata_artifact'

# Generate the pretty metadata artifact
generate_pretty_metadata_artifact(signature_file, timestamp_file, artifact_file)
