# Intentionally awkward exercise input. Improve a COPY, preserving the behavior.
def s(x):
 n=len(x)
 t=sum(x)
 return {"count":n,"total":t,"mean":t/n if n else None}
