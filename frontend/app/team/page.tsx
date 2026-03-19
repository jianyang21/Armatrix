import TeamCard from "@/components/TeamCard";
import { getTeam } from "@/lib/api";

export default async function TeamPage() {
  const team = await getTeam();

  return (
    <div className="min-h-screen bg-black text-white p-8">
      <h1 className="text-4xl font-bold text-center mb-10 text-white">
        Meet Our Team
      </h1>

      <div className="grid gap-6 grid-cols-1 sm:grid-cols-2 md:grid-cols-3">
        {team.map((member: any) => (
          <TeamCard key={member.id} {...member} />
        ))}
      </div>
    </div>
  );
}