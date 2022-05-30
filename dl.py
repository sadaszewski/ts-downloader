import subprocess
import os

for i in range(211, 786 + 1):
  fname = f'{i:08d}.ts'
  print(fname)
  if os.path.exists(fname):
    print('Skipped.')
    continue
  url = f'https://play.boxcast.com/2022/05/28/115001-em6ahgninqqt9ldwrdqi/480p/{fname}'
  url += '?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wbGF5LmJveGNhc3QuY29tLzIwMjIvMDUvMjgvMTE1MDAxLWVtNmFoZ25pbnFxdDlsZHdyZHFpLzQ4MHAvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY1Mzk1NTIwMH19fV19'
  url += '&Signature=IzwAZHqdJdiRRisbsPLaWUzw5Fd7a291PveNbStGREmbZljv8gz4DNHyVvh1oY~GBWWz-WihcdJhgn89E70Rm92NPwfC2WGFBcB0l90VzcfMzrfiNLiVq0-u1V9I7dUVbyp~QiZlFhDvexy9LwgtLSzovouhBGl-LncvQhrwvuF0ivrdaY7Iwufqe3IfvrQhx~QdJEvOB9eQhmYviI-nZs1-rHR8yf1UpNDkjWm~BrB4pii25i1-vxU-W2zDLpNVXmKls4rpj8pgFegL4eoXHYAW~uS~R2kw9hy~UyUF0Kv99Tvw8hrSvcKEItnTOLCIg4nVXyCBsPQhEybX3pceTQ__'
  url += '&Key-Pair-Id=APKAJ7GUCBQUK6NTWZCA'
  cmd = [ 'curl', url, '--output', fname, '--silent' ]
  subprocess.check_output(cmd)
