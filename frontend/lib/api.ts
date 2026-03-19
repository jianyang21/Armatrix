const BASE_URL = "https://armatrix.onrender.com";

export async function getTeam() {
  const res = await fetch(`${BASE_URL}/team`, {
    cache: "no-store",
  });
  return res.json();
}