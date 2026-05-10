export default function Home() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="text-center">
        <h2 className="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl dark:text-white">
          <span className="block">Investissez intelligemment en</span>
          <span className="block text-brand-primary">Afrique et à l'International</span>
        </h2>
        <p className="mt-3 max-w-md mx-auto text-base text-gray-500 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl dark:text-gray-300">
          Kiibare vous guide pour comprendre les marchés (BRVM, Bons UEMOA), simuler vos gains en FCFA et trouver les meilleurs courtiers locaux. 
        </p>
        <div className="mt-5 max-w-md mx-auto sm:flex sm:justify-center md:mt-8">
          <div className="rounded-md shadow">
            <a href="#" className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-brand-primary hover:bg-blue-700 md:py-4 md:text-lg md:px-10 transition">
              Faire ma simulation
            </a>
          </div>
          <div className="mt-3 rounded-md shadow sm:mt-0 sm:ml-3">
            <a href="#" className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-brand-primary bg-white hover:bg-gray-50 md:py-4 md:text-lg md:px-10 transition">
              Découvrir la Bourse 101
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
