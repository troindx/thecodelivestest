import axios from 'axios';
const BASE_URL = 'http://localhost:8000/api/cats';

interface Cat {
  name: string;
  age: number;
  breed: string;
  vaccinations: Vaccination[];
  image: string;
  id?: string;
}

interface Vaccination {
  type: string;
  date: string;
}

describe('Cat Service E2E Test', () => {
  let createdCatId: string;

  it('should create a cat', async () => {
    const cat: Cat = {
      name: 'Mittens',
      age: 3,
      image: "base64EncodedImage",
      breed: 'Siamese',
      vaccinations: [{ type: 'Rabies', date: '2024-01-01' }]
    };

    const response = await axios.post(BASE_URL, cat);
    createdCatId = response.data;
    expect(createdCatId).toBeDefined();
    //Check that createdCatId is of type ObjectId
    expect(createdCatId).toMatch(/^[0-9a-fA-F]{24}$/);
  });
  
  it('should retrieve the created cat', async () => {
    const response = await axios.get<Cat>(`${BASE_URL}/${createdCatId}`);
    const retrievedCat = response.data;
    expect(retrievedCat.name).toEqual('Mittens');
    expect(retrievedCat.age).toEqual(3);
    expect(retrievedCat.breed).toEqual('Siamese');
    expect(retrievedCat.vaccinations.length).toEqual(1);
    expect(retrievedCat.vaccinations[0].type).toEqual('Rabies');
    expect(retrievedCat.vaccinations[0].date).toEqual('2024-01-01T00:00:00');
    expect(retrievedCat.id).toEqual(createdCatId);
  });

  it('should update the cat', async () => {
    const updatedCat: Cat = {
      name: 'Whiskers',
      age: 5,
      image: "base64EncodedImage",
      breed: 'Sphynx',
      vaccinations: [{ type: 'Rabies', date: '2024-01-01' }]
    };

    const response = await axios.put(`${BASE_URL}/${createdCatId}`, updatedCat);
    const success = response.data;
    expect(success).toBe(true);

    const updatedResponse = await axios.get<Cat>(`${BASE_URL}/${createdCatId}`);
    const retrievedUpdatedCat = updatedResponse.data;
    expect(retrievedUpdatedCat.name).toEqual('Whiskers');
    expect(retrievedUpdatedCat.age).toEqual(5);
    expect(retrievedUpdatedCat.breed).toEqual('Sphynx');
  });
  
  it('should delete the cat', async () => {
    const response = await axios.delete(`${BASE_URL}/${createdCatId}`);
    const success = response.data;
    expect(success).toBe(true);

    let retrieveResponse = undefined;
    try {
        retrieveResponse = await axios.get<Cat>(`${BASE_URL}/${createdCatId}`);
    } catch (error: any) {
        expect(error.response.status).toEqual(404);
    }
    
    expect(retrieveResponse).toBeUndefined();
  });
});
