import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))