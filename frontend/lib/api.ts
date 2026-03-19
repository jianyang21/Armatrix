const BASE_URL = "http://localhost:8000";

export async function getTeam() {
  const res = await fetch(`${BASE_URL}/team`, {
    cache: "no-store",
  });
  return res.json();
}