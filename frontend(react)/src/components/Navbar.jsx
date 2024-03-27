import { useState } from 'react';


const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <nav className="p-4 backdrop-blur-md bg-white/30 fixed top-0 left-0 right-0 z-10">
      <div className="container mx-auto">
        <div className="flex items-center justify-between">
          <div className="text-[#003366] text-xl font-bold">Recipe Management</div>
          <div className="flex space-x-4">
            <button
              className="text-[#003366] inline-flex items-center justify-center p-2 rounded-md text-xl leading-none border border-transparent lg:hidden"
              onClick={() => setIsMenuOpen(!isMenuOpen)}
            >
              <svg className="h-6 w-6" fill="none" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" viewBox="0 0 24 24" stroke="currentColor">
                {isMenuOpen ? (
                  <path d="M6 18L18 6M6 6l12 12" />
                ) : (
                  <path d="M4 6h16M4 12h16M4 18h16" />
                )}
              </svg>
            </button>
            <div className={`${isMenuOpen ? 'flex' : 'hidden'} lg:flex lg:items-center lg:space-x-4`}>
              <a href="#" className="text-black font-medium transition duration-300 ease-in-out hover:text-blue-700 hover:underline">Home</a>
              <a href="#" className="text-[#003366] font-medium transition duration-300 ease-in-out hover:text-blue-700 hover:underline">Recipes</a>
              <a href="#" className="text-[#003366] font-medium transition duration-300 ease-in-out hover:text-blue-700 hover:underline">About</a>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
