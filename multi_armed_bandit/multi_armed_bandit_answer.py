import random

class bandit:
    
    def __init__(self, content_ids):
        """Initializes a bandit with all of its arms

        :param content_ids: A list of content_ids that will identify
            each arm
        :type content_ids: list of ints
        """
        self.content_stats = {
            content_id: {
                'successes': 0,
                'failures': 0,
            }
            for content_id in content_ids
        }
    
    def choose_arm_via_thompson_sampling(self):
        """Sample once per arm, return ID with largest sample

        Helpful function: random.betavariate(
            successes + 1,
            not_successes + 1,
        )

        :returns: The id of the content chosen
        :rtype: int
        """
        samples = {
            content_id: random.betavariate(
                self.content_stats[content_id]['successes'] + 1,
                self.content_stats[content_id]['failures'] + 1,
            )
            for content_id in self.content_stats
        }
        return max(
            samples,
            key=samples.get,
        )
    
    def update_arm(self, content_id, was_success):
        """Update the stats for a given arm

        :param content_id: The content_id whose stats we want to
            update
        :type content_id: int
        :param was_success: Whether or not that ID was a success
        :type was_success: boolean
        """
        if was_success:
            self.content_stats[content_id]['successes'] += 1
        else:
            self.content_stats[content_id]['failures'] += 1
    

CONTENT_IDS_TO_TRUE_PROBS = {
    100: 0.06,
    200: 0.07,
    300: 0.05,
}

# Bandit simulation
if __name__ == '__main__':
    for n in [100, 1000, 10000, 100000]:
        choices = {
            key: 0.
            for key in CONTENT_IDS_TO_TRUE_PROBS
        }
        simulated_bandit = bandit([key for key in CONTENT_IDS_TO_TRUE_PROBS])
        for _ in range(n):
            content_id = simulated_bandit.choose_arm_via_thompson_sampling()
            simulated_bandit.update_arm(
                content_id=content_id,
                was_success=random.random() < CONTENT_IDS_TO_TRUE_PROBS[content_id],
            )
            choices[content_id] += 1
        best_content_id = max(
            choices,
            key=choices.get,
        )
        print(
            'For {n} rounds, you chose {best_content_id} the most,'
            '({percent}% of the time)'.format(
                n=n,
                best_content_id=best_content_id,
                percent=choices[best_content_id]/n*100,
            )
        )
