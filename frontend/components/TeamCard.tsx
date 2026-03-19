type Props = {
  name: string;
  role: string;
  bio: string;
  photo: string;
  linkedin: string;
};

export default function TeamCard({
  name,
  role,
  bio,
  photo,
  linkedin,
}: Props) {
  return (
  <div className="bg-zinc-900 text-white shadow-lg rounded-2xl p-6 hover:scale-105 transition duration-300">
    <img
      src={photo}
      alt={name}
      className="w-24 h-24 rounded-full mx-auto border-2 border-gray-700"
    />

    <h2 className="text-xl font-semibold text-center mt-4">
      {name}
    </h2>

    <p className="text-gray-400 text-center">{role}</p>

    <p className="text-sm mt-3 text-gray-300 text-center">
      {bio}
    </p>

    <div className="text-center mt-4">
      <a
        href={linkedin}
        target="_blank"
        className="text-blue-400 hover:text-blue-300 transition"
      >
        LinkedIn
      </a>
    </div>
  </div>
    );  
}