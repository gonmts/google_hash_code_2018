std::map<std::pair<int,int>,int> VMCProblem::PBConstraintLEQ(std::vector<int> vars, std::vector<int> weights, int k)
{
    std::map<std::pair<int,int>,int> s_ij =  std::map<std::pair<int,int>,int>(); //aux variables
    std::vector<int> literals = std::vector<int>();

    //Create all auxiliary vars
    for(int i=0; i < vars.size(); i++)
        for(int j=1; j <= k; j++ )
            s_ij[std::pair<int, int>(i, j)] = _varDispatcher->genAux();
    _SATSolver->addVars((int) vars.size() * k);

    //Remove literals whose coefficients are greater than k, and assign them value 0
    std::vector<int> auxVars;
    std::vector<int> auxWeights;
    for(int i=0; i < vars.size(); i++)
    {
        if(weights[i] > k)
        {
            literals.clear();
            literals.push_back(-vars[i]);
            _SATSolver->addClause(literals);
        }
        else
        {
            auxVars.push_back(vars[i]);
            auxWeights.push_back(weights[i]);
        }
    }
    vars = auxVars;
    weights = auxWeights;




    for(int j=1; j <= weights[0]; j++)
    {
        literals.clear();
        literals.reserve(2);

        literals.push_back(-vars[0]);
        literals.push_back(s_ij[std::pair<int,int>(0,j)]);

        _SATSolver->addClause(literals);                                // (-x1 v S1j)
    }


    for(int j=weights[0]+1; j <= k; j++)
    {
        literals.clear();
        literals.reserve(1);

        literals.push_back(- s_ij[std::pair<int,int>(0,j)]);

        _SATSolver->addClause(literals);                                // (-S1j)
    }


    for(int i=1; i < vars.size(); i++)
    {
        for(int j=1; j <= weights[i]; j++)
        {
            literals.clear();
            literals.reserve(2);

            literals.push_back(-vars[i]);
            literals.push_back(s_ij[std::pair<int,int>(i,j)]);

            _SATSolver->addClause(literals);                             // (-xi v Sij)

        }


        for(int j=1; j <= k; j++)
        {
            literals.clear();
            literals.reserve(2);

            literals.push_back(- s_ij[std::pair<int,int>(i-1,j)]);
            literals.push_back(s_ij[std::pair<int,int>(i,j)]);

            _SATSolver->addClause(literals);                             // (-Si-1,j v Sij)
        }

        for(int j=1; j <= k - weights[i]; j++)
        {
            literals.clear();
            literals.reserve(3);

            literals.push_back(- vars[i]);
            literals.push_back(- s_ij[std::pair<int,int>(i-1,j)]);
            literals.push_back(s_ij[std::pair<int,int>(i, j + weights[i] )]);

            _SATSolver->addClause(literals);                             // (-xi v -Si-1,j v Si,j+wi)
        }

        {
            literals.clear();
            literals.reserve(2);

            literals.push_back(- vars[i]);
            literals.push_back(- s_ij[std::pair<int,int>(i-1, k+1-weights[i] )]);

            _SATSolver->addClause(literals);                             // (-xi v -Si-1,k+1-wi)
        }
    }

    return s_ij;
}


/**
 *
 * Encodes a Pseudo Boolean constraint of type w1.x1 + w2.x2 + ... >= k
 */
std::map<std::pair<int,int>,int> VMCProblem::PBConstraintGEQ(std::vector<int> vars, std::vector<int> weights, int k)
{

    int newK = 0;

    for(int i=0; i < weights.size(); i++)
    {
        vars[i] = -vars[i];
        newK += weights[i];
    }
    newK -= k;

    return this->PBConstraintLEQ(vars, weights, newK);
}
