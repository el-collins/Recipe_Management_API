import React from 'react';

const Navbar = () => {
  return (
    <nav className="bg-gray-800 p-4 m-0">
      <div className="container mx-auto">
        <div className="flex items-center justify-between">
          <div className="text-white text-lg font-semibold">Recipe Management</div>
          <div className="flex space-x-4">
            <a href="#" className="text-white">Home</a>
            <a href="#" className="text-white">Recipes</a>
            <a href="#" className="text-white">About</a>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
