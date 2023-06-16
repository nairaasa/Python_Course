"""
There are many different styles of music and many albums exhibit multiple styles. Create a function that takes a list of musical styles from albums and returns how many styles are unique.

Examples
unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
]) ➞ 9

unique_styles([
"Soul",
"House,Folk",
"Trance,Downtempo,Big Beat,House",
"Deep House",
"Soul"
]) ➞ 7
Notes
N/A
"""

def unique_styles(albums):
    all_styles = ",".join(albums).split(",")
    unique_styles = set(all_styles)
    return len(unique_styles)

print(unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
]))