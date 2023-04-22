-- SQLite
-- SELECT albums.name, COUNT(albums.name) AS num_albums FROM albums GROUP BY albums.name HAVING num_albums > 1
SELECT artists._id, artists.name, albums.name FROM artists
    INNER JOIN albums ON albums.artist = artists._id
WHERE albums.name IN
    (SELECT albums.name FROM albums GROUP BY albums.name HAVING COUNT(albums.name) > 1)
ORDER BY albums.name, artists.name