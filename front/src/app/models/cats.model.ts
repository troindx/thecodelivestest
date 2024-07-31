export interface Vaccination {
    type: string;
    date: string;
  }
  
export interface Cat {
    id?: string;
    name: string;
    age: number;
    breed: string;
    image: string;
    vaccinations: Vaccination[];
  }